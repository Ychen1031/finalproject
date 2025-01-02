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
        if '方式' in postback_data:
            if postback_data['方式'] == 'salary':
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text='薪資為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])]
                    )
                )
            elif postback_data['方式'] == 'bonus':
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text='獎金為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])]
                    )
                )
            elif postback_data['方式'] == 'invest':
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text='投資為' + str(postback_data['price']) + '元' + '\n' + '細項: ' + postback_data['詳情'])]
                    )
                )
            data = [
                [str(datetime.date.today()), postback_data['方式'], postback_data['price'], postback_data['詳情']]
            ]
            pish_data(data)
        else:
            app.logger.error("KeyError: '方式' not found in postback_data")