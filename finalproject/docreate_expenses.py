from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
import json
from throw_sheet_expenses import push_data
import datetime
from config import configuration

# 處理支出的 postback 事件
def handle_expenses_postback(event, app):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        # 解析 postback 資料，並處理解析錯誤
        try:
            postback_data = json.loads(event.postback.data)
        except json.JSONDecodeError:
            app.logger.error(f"JSON解析錯誤: {event.postback.data}")
            return

        if '方式' in postback_data:
            expense_type = postback_data['方式']
            price = str(postback_data['price'])
            details = postback_data['詳情']
            
            # 根據支出類型處理回覆訊息
            reply_message = create_expense_message(expense_type, price, details)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[reply_message]
                )
            )
            
            # 儲存支出資料
            data = [
                [str(datetime.date.today()), expense_type, price, details]
            ]
            push_data(data)

        else:
            app.logger.error(f"KeyError: '方式' not found in postback_data: {postback_data}")

# 創建支出訊息的函數
def create_expense_message(expense_type, price, details):
    expense_messages = {
        'food': f'餐飲費為 {price} 元\n細項: {details}',
        'transportation': f'交通費為 {price} 元\n細項: {details}',
        'entertainment': f'娛樂費為 {price} 元\n細項: {details}',
    }

    # 預設返回未知類型訊息
    return TextMessage(text=expense_messages.get(expense_type, f'支出類型: {expense_type}'))