from src.database import db_connection
from src.database import createTable
import pandas as pd
import os
from datetime import datetime
from src.misc import loadEnv
import re


def extract_date_from_filename(file_name):
    match = re.search(r"(\d{8})", file_name)
    if match:
        date_str = match.group(1)
        return datetime.strptime(date_str, '%Y%m%d')
    return None

def process_csv_files(directory):
    createTable.check_and_create_tables()

    connection = db_connection.get_connection()

    if not connection:
        print("[process_csv_files]無法連接到資料庫")
        return

    try:
        cursor = connection.cursor()

        # 查詢已經導入的檔案紀錄
        cursor.execute("SELECT file_name FROM files_imported")
        imported_files = [row[0] for row in cursor.fetchall()]

        # 遍歷資料夾中的所有CSV檔案
        for file_name in os.listdir(directory):
            if file_name.endswith(".csv") and file_name in imported_files:
                print(f"檔案 {file_name} 已導入過")
            elif file_name.endswith(".csv") and file_name not in imported_files:
                file_path = os.path.join(directory, file_name)
                try:
                    df = pd.read_csv(file_path)
                    if df.empty:
                        print(f"檔案 {file_name} 是空的，跳過該檔案")
                        continue
                except pd.errors.EmptyDataError:
                    print(f"檔案 {file_name} 無欄位可解析，跳過該檔案")
                    continue
                except Exception as e:
                    print(f"讀取檔案 {file_name} 時發生錯誤: {e}")
                    continue

                print(f"正在處理檔案: {file_name}")
                current_time = extract_date_from_filename(file_name)
                print(f"檔案日期: {current_time}")
                # 處理每個IP的資料
                for index, row in df.iterrows():
                    ip = row['IP']
                    unit_name = row['單位']
                    
                    if pd.isnull(ip) or pd.isnull(unit_name):
                        print(f"檔案 {file_name} 中的第 {index} 列有缺少IP或單位名稱的資料，跳過該列")
                        continue
                    
                    # 更新ip_unit表
                    cursor.execute(
                        "INSERT INTO ip_unit (ip, unit_name, last_updated) VALUES (%s, %s, %s) "
                        "ON DUPLICATE KEY UPDATE unit_name = VALUES(unit_name), last_updated = VALUES(last_updated)",
                        (ip, unit_name, current_time)
                    )

                    # 更新ip_history表
                    cursor.execute(
                        "SELECT * FROM ip_history WHERE ip = %s ORDER BY start_time DESC LIMIT 1",
                        (ip,)
                    )
                    history = cursor.fetchone()
                    if history:
                        last_unit_name = history[2]
                        last_start_time = history[3]
                        if last_unit_name != unit_name:
                            cursor.execute(
                                "UPDATE ip_history SET end_time = %s WHERE id = %s",
                                (current_time, history[0])
                            )
                            cursor.execute(
                                "INSERT INTO ip_history (ip, unit_name, start_time) VALUES (%s, %s, %s)",
                                (ip, unit_name, current_time)
                            )
                    else:
                        cursor.execute(
                            "INSERT INTO ip_history (ip, unit_name, start_time) VALUES (%s, %s, %s)",
                            (ip, unit_name, current_time)
                        )

                # 將檔案名稱插入files_imported表
                cursor.execute(
                    "INSERT INTO files_imported (file_name) VALUES (%s)",
                    (file_name,)
                )

        # 提交變更
        connection.commit()

    except db_connection.Error as e:
        print(f"資料庫操作時發生錯誤: {e}")
        connection.rollback()
        

    finally:
        if connection.is_connected():
            connection.close()
            print("資料庫連線已關閉")

def process_files_from_directory(directory='./data/nchu_top1000_data'):
    process_csv_files(directory)
