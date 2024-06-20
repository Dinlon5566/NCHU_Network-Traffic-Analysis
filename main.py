from src.trafficCapture import fetch_nchu_traffic
from src.test import loadEnv
from dotenv import load_dotenv
import os

def main():
    cmd=input("Secevt 1 to load env, 2 to fetch nchu traffic: ")
    if cmd == '1':
        loadEnv.printEnv()
    elif cmd == '2':
        fetch_nchu_traffic.main()
        
    

if __name__ == '__main__':
    main()
