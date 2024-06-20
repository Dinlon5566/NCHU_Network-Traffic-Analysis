# example_usage.py
from src.database import db_connection


def connect_to_test():
    connection = db_connection.get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM test")
            results = cursor.fetchall()
            for row in results:
                print(row)
        except db_connection.Error as e:
            print(f"資料庫操作時發生錯誤: {e}")
        finally:
            if connection.is_connected():
                connection.close()
                print("資料庫連線已關閉")
