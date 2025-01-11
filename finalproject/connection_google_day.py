import requests
import base64
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

# Google Apps Script Web Apps URL
url = os.getenv('GOOGLEDAY')  # 替換為部署後的 URL
def get_ngrok_public_url(工作表):
    # 發送 POST 請求
    data = {"sheetName": 工作表}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        if result["status"] == "success":
            if "imageBase64" in result:
                # 解碼 Base64 圖片
                image_data = result["imageBase64"].split(",")[1]  # 去除 Data URI 前綴
                img = Image.open(BytesIO(base64.b64decode(image_data)))
                img.save("static/chart.png")  # 保存圖片
            else:
                print("錯誤：'imageBase64' 鍵不存在")
        else:
            print("錯誤訊息：", result["message"])
    else:
        print("HTTP 請求失敗，狀態碼：", response.status_code)
    return '本日彙總'

# get_ngrok_public_url('2024-11-26create支出')