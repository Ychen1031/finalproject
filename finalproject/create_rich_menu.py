from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    MessagingApiBlob
)
import requests
import json
from config import configuration

def create_rich_menu():
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_blob_api = MessagingApiBlob(api_client)

        # Create rich menu
        headers = {
            'Authorization': 'Bearer ' + configuration.access_token,
            'Content-Type': 'application/json'
        }
        body = {
            "size": {
                "width": 2500,
                "height": 1686
            },
            "selected": True,
            "name": "圖文選單 1",
            "chatBarText": "查看更多資訊",
            "areas": [
                {
                    "bounds": {
                        "x": 0,
                        "y": 0,
                        "width": 833,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"支出"}',
                        "text": "請輸入支出詳情ex:100 炒飯"
                    }
                },
                {
                    "bounds": {
                        "x": 834,
                        "y": 0,
                        "width": 833,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"收入"}',
                        "text": "請輸入收入詳情ex:100 台積電"
                    }
                },
                {
                    "bounds": {
                        "x": 1663,
                        "y": 0,
                        "width": 834,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"分析"}',
                        "text": "開始分析"
                    }
                },
                {
                    "bounds": {
                        "x": 0,
                        "y": 843,
                        "width": 833,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"本日彙總"}',
                        "text": "產生本日彙總"
                    }
                },
                {
                    "bounds": {
                        "x": 834,
                        "y": 843,
                        "width": 833,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"本月彙總"}',
                        "text": "產生本月彙總"
                    }
                },
                {
                    "bounds": {
                        "x": 1662,
                        "y": 843,
                        "width": 838,
                        "height": 843
                    },
                    "action": {
                        "type": "postback",
                        "data": '{"action" :"回饋"}',
                        "text": "產生回饋與建議中"
                    }
                }
            ]
        }

        response = requests.post('https://api.line.me/v2/bot/richmenu', headers=headers, data=json.dumps(body).encode('utf-8'))
        response = response.json()
        # print(response)
        rich_menu_id = response["richMenuId"]
        
        # Upload rich menu image
        with open('static/richmenu-2.png', 'rb') as image:
            line_bot_blob_api.set_rich_menu_image(
                rich_menu_id=rich_menu_id,
                body=bytearray(image.read()),
                _headers={'Content-Type': 'image/jpeg'}
            )

        line_bot_api.set_default_rich_menu(rich_menu_id)
