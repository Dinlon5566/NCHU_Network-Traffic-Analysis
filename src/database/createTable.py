from src.database import db_connection

# 建立資料表的函數


def check_and_create_tables():
    connection = db_connection.get_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # 檢查資料表是否存在
            cursor.execute("""
                SELECT COUNT(*) FROM information_schema.tables 
                WHERE table_schema = DATABASE() 
                AND table_name IN ( 'IP_Unit', 'IP_History', 'Files_Imported')
            """)
            result = cursor.fetchone()

            # 如果有一個或多個資料表不存在，則創建所有資料表
            if result[0] < 3:
                print("[CheckAndCreateTables]有一個或多個資料表不存在，開始創建資料表")
                create_tables()
            else:
                print("所有資料表已存在")

        except db_connection.Error as e:
            print(f"資料庫操作時發生錯誤: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("[CheckAndCreateTables] 資料庫連線已關閉")
    else:
        print("[CheckAndCreateTables] 無法連線到資料庫")
        
def create_tables():
    connection = db_connection.get_connection()
    if connection:
        try:
            cursor = connection.cursor()

            # 建立 IP_Unit
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ip_unit (
                    ip VARCHAR(15) NOT NULL PRIMARY KEY,
                    unit_name VARCHAR(255) NOT NULL,
                    last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                )
            """)
            print("資料表 'ip_unit' 已建立")

            # 建立 ip_history
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ip_history (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    ip VARCHAR(15) NOT NULL,
                    unit_name VARCHAR(255) NOT NULL,
                    start_time TIMESTAMP NOT NULL,
                    end_time TIMESTAMP
                )
            """)
            print("資料表 'ip_history' 已建立")

            # 建立 files_imported
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS files_imported (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    file_name VARCHAR(255) NOT NULL,
                    import_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("資料表 'files_imported' 已建立")

        except db_connection.Error as e:
            print(f"[CreateTables]資料庫操作時發生錯誤: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("[CreateTables] 資料庫連線已關閉")
    else:
        print("[CreateTables] 無法連線到資料庫")


