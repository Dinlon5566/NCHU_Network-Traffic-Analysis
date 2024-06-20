import sys
import os
from dotenv import load_dotenv
from src.trafficCapture import fetch_nchu_traffic
from src.misc import loadEnv
from src.database import importData
from src.mytest import db_example

sys.path.append('./src')


def main():
    cmd = input("選擇 1 進入測試, 2 擷取特定日期流量, 3 檢查資料夾並導入資料, 4 導引模式(推薦):")
    if cmd == '1':
        print("進入測試模式")
        cmd = input("選擇 1 列印環境變數, 2 連接到測試數據庫:")
        if cmd == '1':
            loadEnv.printEnv()
        elif cmd == '2':
            db_example.connect_to_test()
    elif cmd == '2':
        fetch_nchu_traffic.main()
    elif cmd == '3':
        importData.process_files_from_directory()
    elif cmd == '4':
        fetch_nchu_traffic.main()
        print("流量擷取完成")
        importData.process_files_from_directory()
        print("資料導入完成")
        


if __name__ == '__main__':
    main()
