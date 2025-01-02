import gspread
import datetime
from config import getdocsgoogle
gc = gspread.service_account(filename='token.json')
sh = gc.open_by_url(getdocsgoogle())

def pish_data(data):
    try:
        today = datetime.date.today().strftime("%Y-%m-%d") + 'create收入'
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
