# 這個是抓取流量的原形程式碼，自動化請使用 fetchNetRange
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import csv
from datetime import datetime


# 忽略不安全的請求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 目標URL
url = 'https://top100.nchu.edu.tw/nchubody2.php'
date = '2024-05-01'
url = f"{url}?date={date}"

try:
    # 發送請求，忽略 SSL 憑證驗證
    response = requests.get(url ,verify=False)
    
    # 檢查回應狀態碼
    if response.status_code == 200:
        print("成功連線到網站")
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取報表產生時間
        report_time_element = soup.find('td', text=lambda x: x and '報表產生時間' in x)
        report_time_text = report_time_element.text.strip()
        report_time = report_time_text.split('報表產生時間: ')[-1]
        if '24:00' in report_time:
            report_time = report_time.replace('24:00', '00:00')
        report_time_obj = datetime.strptime(report_time, '%Y-%m-%d %H:%M')
        timestamp = report_time_obj.strftime('%Y%m%d_%H%M%S')

        
        
        # 定義需要提取的表格ID列表
        table_ids = [
            'account_list_1', 'account_list_101', 'account_list_201',
            'account_list_301', 'account_list_401', 'account_list_501',
            'account_list_601', 'account_list_701', 'account_list_801',
            'account_list_901'
        ]
        
        all_data = []

        for table_id in table_ids:
            table = soup.find('table', {'id': table_id})
            if table:
                rows = table.find_all('tr')
                for row in rows[1:]:  # 忽略標題行
                    cols = row.find_all('td')
                    cols = [ele.text.strip() for ele in cols]
                    all_data.append(cols)
        

        # 定義CSV文件名
        csv_filename = f"nchu_top1000_{timestamp}.csv"
        
        # 將數據寫入CSV文件
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['名次', '單位', 'IP', 'IN', 'OUT', '總流量'])
            csvwriter.writerows(all_data)
        print(f"數據已成功保存到 {csv_filename}")
    else:
        print(f"無法連線到網站，狀態碼: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"請求錯誤: {e}")
