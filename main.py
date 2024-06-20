import sys
import os
from dotenv import load_dotenv
from src.trafficCapture import fetch_nchu_traffic
from src.misc import loadEnv
from src.database import importData
from src.mytest import db_example

sys.path.append('./src')

def main():
    cmd = input("Secevt 1 to TEST, 2 to fetch nchu traffic, 3 to import data,4 to Auto :")
    if cmd == '1':
        print("TEST mode")
        cmd = input("Secevt 1 to printEnv, 2 to connect_to_database:")
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
        print("fetch_nchu_traffic done")
        importData.process_files_from_directory()
        print("importData done")
        


if __name__ == '__main__':
    main()
