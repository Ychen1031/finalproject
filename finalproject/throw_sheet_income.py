import gspread
import datetime
from config import getdocsgoogle

def get_worksheet(sh, title):
    try:
        return sh.worksheet(title)
    except gspread.exceptions.WorksheetNotFound:
        worksheet = sh.add_worksheet(title=title, rows="100", cols="20")
        worksheet.insert_row(['日期', '方式', 'price', '詳情'], 1)
        return worksheet

def push_data(data):
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
