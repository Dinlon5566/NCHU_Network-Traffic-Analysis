# fetch_nchu_traffic.py
from datetime import datetime
from src.trafficCapture import fetchNetRange
from src.misc import loadEnv
import os


def main():
    # 輸入開始時間和結束時間
    start_date_input = input('請輸入開始時間 (YYYY-MM-DD): ')
    end_date_input = input('請輸入結束時間 (YYYY-MM-DD): ')
    
    folder = './data/nchu_top1000_data'

    # 解析時間字串為 datetime 物件
    start_date = datetime.strptime(start_date_input, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_input, '%Y-%m-%d')

    # 建立資料夾如果它不存在
    os.makedirs(folder, exist_ok=True)

    # 呼叫 fetchNetRange 的方法來獲取資料
    fetchNetRange.fetch_data_in_range(start_date, end_date, folder)


if __name__ == '__main__':
    main()
