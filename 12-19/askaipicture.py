# import os
# import google.generativeai as generativeai

# generativeai.configure(api_key='AIzaSyD-OynJBPmfxNCHaQaj09Pyr864amOV8zE')
# response = generativeai.GenerativeModel('gemini-2.0-flash-exp').generate_content('你是誰')
# print(response.text)  # '你是誰'的回應

import os
import google.generativeai as generativeai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('GEMINIAPIKEY'))
generativeai.configure(api_key=os.getenv('GEMINIAPIKEY')) # 請替換成您的 API 金鑰

model = generativeai.GenerativeModel('gemini-2.0-flash-exp') # 注意：需要使用支援 vision 的模型

image_path = r'12-19\chart_month.png' # 請替換成您的圖片路徑

try:
    img = Image.open(image_path)
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    contents = [
        {
            "parts": [ # 關鍵修改：使用 "parts" 包裹圖像和文本
                {
                    "mime_type": "image/jpeg",
                    "data": image_data
                },
                {
                    "text": "這是一張收入和支出的圖" # 文本部分直接使用 "text" 鍵
                }
            ]
        }
    ]

    response = model.generate_content(contents)
    print(response.text)
except FileNotFoundError:
    print(f"找不到圖片檔案：{image_path}")
except Exception as e:
    print(f"發生錯誤：{e}")