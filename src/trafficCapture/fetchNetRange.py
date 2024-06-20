# automain.py
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime, timedelta

# 忽略不安全的請求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 定義需要提取的表格ID列表
table_ids = [
    'account_list_1', 'account_list_101', 'account_list_201',
    'account_list_301', 'account_list_401', 'account_list_501',
    'account_list_601', 'account_list_701', 'account_list_801',
    'account_list_901'
]


def fetch_data_for_date(date, folder_path):
    # 預先確定CSV文件名
    report_time_obj = datetime.strptime(date, '%Y-%m-%d')
    timestamp = report_time_obj.strftime('%Y%m%d_000000')  # 預設時間
    csv_filename = os.path.join(folder_path, f"nchu_top1000_{timestamp}.csv")

    # 檢查文件是否已存在
    if os.path.exists(csv_filename):
        print(f"檔案 {csv_filename} 已存在，跳過下載。")
        return  # 如果文件存在，直接返回不進行連線

    url = f'https://top100.nchu.edu.tw/nchubody2.php?date={date}'
    try:
        # 發送請求，忽略 SSL 憑證驗證
        response = requests.get(url, verify=False)

        # 檢查回應狀態碼
        if response.status_code == 200:
            print(f"成功連線到網站: {date}")

            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            all_data = []

            for table_id in table_ids:
                table = soup.find('table', {'id': table_id})
                if table:
                    rows = table.find_all('tr')
                    for row in rows[1:]:  # 忽略標題行
                        cols = row.find_all('td')
                        cols = [ele.text.strip() for ele in cols]
                        all_data.append(cols)

            # 將數據寫入CSV文件
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(['名次', '單位', 'IP', 'IN', 'OUT', '總流量'])
                csvwriter.writerows(all_data)
            print(f"數據已成功保存到 {csv_filename}")
        else:
            print(f"無法連線到網站，狀態碼: {response.status_code} 日期: {date}")
    except requests.exceptions.RequestException as e:
        print(f"請求錯誤: {e} 日期: {date}")


def fetch_data_in_range(start_date, end_date, folder_path):
    os.makedirs(folder_path, exist_ok=True)

    current_date = start_date
    while current_date <= end_date:
        fetch_data_for_date(current_date.strftime('%Y-%m-%d'), folder_path)
        current_date += timedelta(days=1)
