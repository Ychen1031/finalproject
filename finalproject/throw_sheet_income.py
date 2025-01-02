from flask import Flask, request, abort
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
    PostbackEvent
)
import json
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets 認證
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path/to/your/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("IncomeSheet").sheet1

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(PostbackEvent)
def handle_postback_event(event):
    if event.postback.data:
        try:
            postback_data = json.loads(event.postback.data)
            if postback_data['action'] == '收入':
                handle_income_postback(event, app)
            else:
                app.logger.error(f"Unknown action: {postback_data['action']}")
        except json.JSONDecodeError as e:
            app.logger.error(f"JSONDecodeError: Invalid JSON data - {e}")
            app.logger.error(f"Raw data: {event.postback.data}")
    else:
        app.logger.error("Empty postback data")

def handle_income_postback(event, app):
    postback_data = json.loads(event.postback.data)
    方式 = postback_data.get('方式')
    price = postback_data.get('price')
    details = postback_data.get('詳情')

    方式描述 = {
        'salary': '薪資為',
        'bonus': '獎金為',
        'invest': '投資為'
    }

    if 方式 in 方式描述:
        response_message = f"{方式描述[方式]}{price}元\n細項: {details}"
        # 將收入記錄到 Google Sheets
        sheet.append_row([datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 方式, price, details])
    else:
        response_message = "未知的方式"

    reply_message = TextMessage(text=response_message)
    reply_request = ReplyMessageRequest(reply_token=event.reply_token, messages=[reply_message])
    messaging_api = MessagingApi(ApiClient(Configuration()))
    messaging_api.reply_message(reply_request)

if __name__ == "__main__":
    app.run(port=5000)