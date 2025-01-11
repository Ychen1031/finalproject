import time
import gspread
import datetime
from config import getdocsgoogle

def get_worksheet(sh, title):
    try:
        worksheet = sh.worksheet(title)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=title, rows="100", cols="20")
        worksheet.insert_row(['日期', '方式', '價錢', '詳情'], 1)
    return worksheet

def push_data(data):
    start_time = time.time()
    
    gc = gspread.service_account(filename='token.json')
    sh = gc.open_by_url(getdocsgoogle())
    
    today = datetime.date.today().strftime("%Y-%m-%d") + 'create收入'
    worksheet = get_worksheet(sh, today)
    
    try:
        worksheet.insert_rows(data, 2)
        print('成功加入數據!')
    except Exception as e:
        print('加入數據失敗!')
        print(e)
    
    end_time = time.time()
    print(f"執行時間: {end_time - start_time} 秒")

# # 測試 push_data 函數
# data = [['2023-10-01', '現金', '1000', '收入詳情']]
# push_data(data)