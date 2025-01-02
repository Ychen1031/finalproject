from linebot.v3.messaging import (
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    QuickReply,
    QuickReplyItem,
    PostbackAction
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from config import configuration, handler

def create_quick_reply_items(action, amount, details):
    options = ['薪資', '獎金', '投資']
    items = [
        QuickReplyItem(
            action=PostbackAction(
                label=option,
                data=f'{{"action": "{action}", "方式": "{option.lower()}", "price": {amount}, "詳情": "{details}"}}'
            )
        ) for option in options
    ]
    return items

def income(action):
    @handler.add(MessageEvent, message=TextMessageContent)
    def handle_message(event):
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            user_message = event.message.text.split(' ')
            
            if user_message[0].isdigit():
                amount = int(user_message[0])
                details = user_message[1]
                quick_reply_items = create_quick_reply_items(action, amount, details)
                
                reply_message_request = ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[TextMessage(text='請選擇此收入明細', quick_reply=QuickReply(items=quick_reply_items))]
                )
                
                line_bot_api.reply_message_with_http_info(reply_message_request)
    return