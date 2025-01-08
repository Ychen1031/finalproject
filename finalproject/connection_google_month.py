import requests
import base64
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os
from datetime import datetime
load_dotenv()

url = os.getenv('GOOGLEMONTH')  # 替換為部署後的 URL

def get_chart(yearMonth):
    data = {"yearMonth": yearMonth}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        try:
            result = response.json()
            if result["status"] == "success":
                if "imageBase64" in result:
                    image_data = result["imageBase64"].split(",")[1]
                    img = Image.open(BytesIO(base64.b64decode(image_data)))
                    img.save(f"static/chart_month.png") #檔名包含年月
                    print(f"圖片已儲存至 static/{yearMonth}_chart.png")
                else:
                    print("錯誤：'imageBase64' 鍵不存在")
            else:
                print("Apps Script 錯誤訊息：", result["message"])
        except ValueError as e:
            print(f"JSON 解析錯誤：{e}，回應內容：{response.text}")
    else:
        print("HTTP 請求失敗，狀態碼：", response.status_code)
        print("回應內容:", response.text)
    return '本月彙總'
# 測試範例
current_year_month = datetime.now().strftime("%Y-%m")
get_chart(current_year_month)
