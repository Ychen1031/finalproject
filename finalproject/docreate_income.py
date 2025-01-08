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

        # 解析 postback 資料，並處理解析錯誤
        try:
            postback_data = json.loads(event.postback.data)
        except json.JSONDecodeError:
            app.logger.error(f"JSON解析錯誤: {event.postback.data}")
            return

        if '方式' in postback_data:
            income_type = postback_data['方式']
            price = str(postback_data['price'])
            details = postback_data['詳情']
            
            # 根據收入類型處理回覆訊息
            reply_message = create_income_message(income_type, price, details)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[reply_message]
                )
            )
            
            # 儲存收入資料
            data = [
                [str(datetime.date.today()), income_type, price, details]
            ]
            pish_data(data)

        else:
            app.logger.error(f"KeyError: '方式' not found in postback_data: {postback_data}")

# 創建收入訊息的函數
def create_income_message(income_type, price, details):
    income_messages = {
        'salary': f'薪資為 {price} 元\n細項: {details}',
        'bonus': f'獎金為 {price} 元\n細項: {details}',
        'investment': f'投資收入為 {price} 元\n細項: {details}',
    }

    # 預設返回未知類型訊息
    return TextMessage(text=income_messages.get(income_type, f'未知收入類型: {income_type}'))
