import mysql.connector
from mysql.connector import Error
from src.misc import loadEnv
from dotenv import load_dotenv
import os


def connect_to_database():
    load_dotenv()
    print("Environment Variables:")
    db_user = loadEnv.check_and_set_env_var("DB_USER")
    db_pass = loadEnv.check_and_set_env_var("DB_PASSWORD")
    db_host = loadEnv.check_and_set_env_var("DB_HOST")
    db_name = loadEnv.check_and_set_env_var("DB_NAME")
    db_port = loadEnv.check_and_set_env_var("DB_PORT")
    try:
        # 建立資料庫連線
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
            port=db_port
        )

        if connection.is_connected():
            print("成功連接到資料庫")
            # 可以在這裡執行其他資料庫操作
            # cursor = connection.cursor()
            # cursor.execute("SELECT DATABASE();")
            # record = cursor.fetchone()
            # print("目前使用的資料庫:", record)

    except Error as e:
        print(f"連接資料庫時發生錯誤: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("資料庫連線已關閉")


if __name__ == "__main__":
    connect_to_database()
