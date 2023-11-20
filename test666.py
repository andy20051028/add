from flask import Flask, request
import json
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    try:
        json_data = json.loads(body)
        access_token = '8dCcApp2pCuMp/lF9VywQ4s74qJ9uyPT0JqyweZjouJfJNX+4CzoQDa+VyddmfRx1MAdarIcA+GXae/o8Nsq6Qqy1Z+F1iVcsXbXpV0/sEEPny+nrmzKaWINa8+C0gcFjQXdPE9COpPliJ2OrTddUgdB04t89/1O/w1cDnyilFU='
        secret = '3575a093da384e0e43089f871ddbb8ba'
        line_bot_api = LineBotApi(access_token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        type = json_data['events'][0]['message']['type']

        if type == 'text':
            msg = json_data['events'][0]['message']['text']
            print(msg)

            # Check if the received message is "你好"
            if msg == '桃園哪裡好玩?':
                reply = '我的感情'
            else:
                reply = '你傳的不是「你好」呦～'
            print(reply)

            line_bot_api.reply_message(tk, TextSendMessage(text=reply))
        else:
            reply = '你傳的不是文字呦～'
            print(reply)
            line_bot_api.reply_message(tk, TextSendMessage(text=reply))

    except Exception as e:
        print(f"Error: {e}")
        print(body)

    return 'OK'

if __name__ == "__main__":
    app.run()
