from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TemplateMessage,
    ConfirmTemplate,
    ButtonsTemplate,
    CarouselTemplate,
    CarouselColumn,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    MessageAction,
    URIAction,
    PostbackAction,
    DatetimePickerAction,
    CameraAction,
    CameraRollAction,
    LocationAction
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)
from config import configuration
import requests
from config import handler

response = requests.get('http://localhost:4040/api/tunnels')
response = response.json()

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        url = response['tunnels'][0]['public_url'] + '/static/Logo.png'
        carousel_template = CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=url,
                    title='技術支援',
                    text='若有任何問題，請聯繫開發團隊：\n指導教授：謝文川專題\n學生：吳書逸、陳禹璋、李宇辰、林慧蘭、黃健程',
                    actions=[
                        URIAction(
                            label='按我前往 GitHub',
                            uri='https://github.com/Ychen1031/finalproject'
                        )
                    ]
                ),
            ]
        )
        carousel_message = TemplateMessage(
            alt_text='這是 Carousel Template',
            template=carousel_template
        )

        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages =[carousel_message]
            )
        )