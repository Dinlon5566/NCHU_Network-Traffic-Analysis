# main.py
import argparse
from datetime import datetime
import fetchNetRange

def main():
    parser = argparse.ArgumentParser(description='Fetch traffic data for NCHU.')
    parser.add_argument('--ts', required=True, help='Start date in YYYY-MM-DD format')
    parser.add_argument('--te', required=True, help='End date in YYYY-MM-DD format')
    parser.add_argument('-f', default='nchu_top1000_data', help='Folder to save the data')

    args = parser.parse_args()
    start_date=args.ts
    end_date=args.te
    folder=args.f
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    folder_path = folder

    fetchNetRange.fetch_data_in_range(start_date, end_date, folder_path)

if __name__ == '__main__':
    main()
