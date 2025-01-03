import os
from flask import Flask
from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.messaging import (
    Configuration
)
from dotenv import load_dotenv

load_dotenv()

configuration = Configuration(access_token=os.getenv('LINE_BOT_API'))
handler = WebhookHandler(os.getenv('LINE_BOT_HANDLER'))
def getdocsgoogle():
    return os.getenv('DOCSGOOGLE')
def getgoogleday():
    return os.getenv('GOOGLEDAY')
def getgooglemonth():
    return os.getenv('GOOGLEMONTH')

