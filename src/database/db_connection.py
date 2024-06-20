import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import sys
from src.misc import loadEnv

load_dotenv()

def connect_to_database():
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
            print("[db_connection]成功連接到資料庫")
            
    except Error as e:
        print(f"[db_connection]連接資料庫時發生錯誤: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("[db_connection]資料庫連線已關閉")


def get_connection():
    db_user = loadEnv.check_and_set_env_var("DB_USER")
    db_pass = loadEnv.check_and_set_env_var("DB_PASSWORD")
    db_host = loadEnv.check_and_set_env_var("DB_HOST")
    db_name = loadEnv.check_and_set_env_var("DB_NAME")
    db_port = loadEnv.check_and_set_env_var("DB_PORT")
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            database=db_name,
            port=db_port
        )
        if connection.is_connected():
            print("[db_connection]成功連接到資料庫")
            return connection
    except Error as e:
        print(f"[db_connection]連接資料庫時發生錯誤: {e}")
        return None


if __name__ == "__main__":
    connect_to_database()
