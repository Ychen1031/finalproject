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
    print('製作中...')
    
if __name__ == "__main__":
    app.run(port=5000)