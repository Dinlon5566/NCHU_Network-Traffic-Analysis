import sys
import os
from dotenv import load_dotenv
from src.trafficCapture import fetch_nchu_traffic
from src.misc import loadEnv
from src.database import crateTable
from src.mytest import db_example

sys.path.append('./src')

def main():
    cmd = input("Secevt 1 to TEST, 2 to fetch nchu traffic: ")
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
        crateTable.check_and_create_tables()


if __name__ == '__main__':
    main()
