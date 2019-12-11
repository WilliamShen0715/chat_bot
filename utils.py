import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"
def send_image_message(reply_token,text):
    line_bot_api = LineBotApi(channel_access_token)
    if text=="image":
        line_bot_api.reply_message(reply_token,ImageSendMessage(original_content_url='https://i.ibb.co/jgD2vvc/lab1.jpg', preview_image_url='https://i.ibb.co/jgD2vvc/lab1.jpg'))

"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
#%%
import random as rand
#ans = rand.randint(1,100)
#chances = 5
def play():
    return rand.randint(1,100)
def game(guess,ans):
    if ans == guess:return 0
    else: return -1
