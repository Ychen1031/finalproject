from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
import json
from throw_sheet_income import pish_data
import datetime
from config import configuration

# 處理收入的 postback 事件
def handle_income_postback(event, app):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        postback_data = json.loads(event.postback.data)
        print(type(postback_data))
        
        income_type = postback_data.get('方式')
        if income_type:
            handle_income_type(income_type, postback_data, event.reply_token, line_bot_api)

def handle_income_type(income_type, postback_data, reply_token, line_bot_api):
    if income_type == 'salary':
        reply_message = create_salary_message(postback_data)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=reply_token,
                messages=[reply_message]
            )
        )

def create_salary_message(postback_data):
    price = postback_data.get('price', '未知')
    details = postback_data.get('詳情', '無')
    return TextMessage(text=f'薪資為 {price} 元\n細項: {details}')