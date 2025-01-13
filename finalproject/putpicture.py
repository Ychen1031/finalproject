from linebot.v3.messaging import (
    MessagingApi
)
from linebot.v3.messaging import (
    MessagingApi,
    ImageMessage,
    ApiClient,
    ReplyMessageRequest
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from config import configuration, handler
import requests

response = requests.get('http://localhost:4040/api/tunnels')
response = response.json()

def putpicture(Options):
    print('putpicture')
    @handler.add(MessageEvent, message=TextMessageContent)
    def handle_message(event):
        text = event.message.text
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
        # 取得圖片網址
        if Options == "本日彙總":
            url = response['tunnels'][0]['public_url'] + '/static/chart.png'
        elif Options == "本月彙總":
            url = response['tunnels'][0]['public_url'] + '/static/chart_month.png'
        # 回覆圖片
        line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(original_content_url=url, preview_image_url=url)
                    ]
                )
            )
