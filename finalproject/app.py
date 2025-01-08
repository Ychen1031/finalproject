from flask import Flask, request, abort
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    QuickReply,
    QuickReplyItem,
    PostbackAction,
    MessageAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    PostbackEvent
)
from config import configuration, handler
from docreate_income import handle_income_postback
from docreate_expenses import handle_expenses_postback
from expenses import expenses
from income import income
from connection_google_day import get_ngrok_public_url
from putpicture import putpicture
from connection_google_month import get_chart
from askaipicture import ask_ai
import json
import datetime
import time

工作表 = ''

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# 獲得create_rich_menu和docreate_expenses.py的postback事件
@handler.add(PostbackEvent)
def handle_postback_event(event):
    global 工作表
    if event.postback.data:
        try:
            postback_data = json.loads(event.postback.data)
            print(postback_data)
            print(type(postback_data))
            print(postback_data)  # 添加此行以打印解析後的 JSON 數據
            if postback_data['action'] == '支出':
                工作表 = datetime.date.today().strftime("%Y-%m-%d") + 'create支出'
                expenses(postback_data['action'])
                handle_expenses_postback(event, app)
            elif postback_data['action'] == '收入':
                工作表 = datetime.date.today().strftime("%Y-%m-%d") + 'create收入'
                income(postback_data['action'])
                handle_income_postback(event, app)
            elif postback_data['action'] == '本日彙總':
                print('本日彙總')
                print(工作表)
                Options = get_ngrok_public_url(工作表)
                time.sleep(10)
                putpicture(Options)
            elif postback_data['action'] == '本月彙總':
                print('本月彙總')
                Options = get_chart(datetime.date.today().strftime("%Y-%m"))
                time.sleep(10)
                putpicture(Options)
            elif postback_data['action'] == '分析':
                print('分析')
                response=ask_ai()
                with ApiClient(configuration) as api_client:
                    line_bot_api = MessagingApi(api_client)
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=event.reply_token,
                            messages=[TextMessage(text=response)]
                        )
                    )
            elif postback_data['action'] == '回饋':
                print('回饋')
                response='請至GitHub，留言給我們，網址:https://github.com/database-playground/app-sf'
                with ApiClient(configuration) as api_client:
                    line_bot_api = MessagingApi(api_client)
                    line_bot_api.reply_message_with_http_info(
                        ReplyMessageRequest(
                            reply_token=event.reply_token,
                            messages=[TextMessage(text=response)]
                        )
                    )
            else:
                app.logger.error(f"KeyError: 'action' not found in postback_data - {postback_data}")
        except json.JSONDecodeError as e:
            app.logger.error(f"JSONDecodeError: Invalid JSON data - {e}")
            app.logger.error(f"Raw data: {event.postback.data}")
    else:
        app.logger.error("Empty postback data")
    
from create_rich_menu import create_rich_menu

create_rich_menu()

if __name__ == "__main__":
    app.run(port=5000)