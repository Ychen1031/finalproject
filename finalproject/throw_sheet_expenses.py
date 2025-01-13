import gspread
import datetime
from config import getdocsgoogle
gc = gspread.service_account(filename='token.json')

sh = gc.open_by_url(getdocsgoogle())

def push_data(data):
    try:
        today = datetime.date.today().strftime("%Y-%m-%d") + 'create支出'
        worksheet = sh.worksheet(today)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=today, rows="100", cols="20")
        worksheet.insert_row(['日期', '方式', 'price', '詳情'], 1)
    try:
        worksheet.insert_rows(data, 2)
        print('成功加入數據!')
    except Exception as e:
        print('加入數據失敗!')
        print(e)

# worksheet = sh.get_worksheet(0)

# data = [
#     ['早餐', 3 ,'蛋炒飯'],
#     ['午餐', 50, '炒麵'],
#     ['晚餐', 70, '炒飯']
# ]

# worksheet.insert_rows( data, 2)

# print('成功加入數據!')