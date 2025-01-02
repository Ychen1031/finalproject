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

# 輸出line按鈕回傳POST請求
def income(action):
    @handler.add(MessageEvent, message=TextMessageContent)
    def handle_message(event):
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            usermassage = event.message.text.split(' ')
            
            print(type(usermassage[0]))
            if usermassage[0].isdigit():
                usermassage[0] = int(usermassage[0])
                line_bot_api.reply_message_with_http_info(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text='請選擇此收入明細', quick_reply=QuickReply(items=[
                            QuickReplyItem(action=PostbackAction(label='薪資', data='{"action": "' + action + '", "方式": "salary", "price": ' + str(usermassage[0]) + ', "詳情": "' + usermassage[1] + '"}')),
                            QuickReplyItem(action=PostbackAction(label='獎金', data='{"action": "' + action + '", "方式": "bonus", "price": ' + str(usermassage[0]) + ', "詳情": "' + usermassage[1] + '"}')),
                            QuickReplyItem(action=PostbackAction(label='投資', data='{"action": "' + action + '", "方式": "invest", "price": ' + str(usermassage[0]) + ', "詳情": "' + usermassage[1] + '"}'))
                        ]))]
                    )
                )
    return
