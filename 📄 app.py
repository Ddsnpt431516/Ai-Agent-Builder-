from flask import Flask, request
import telegram

app = Flask(__name__)
bot = telegram.Bot(token="तुझं-बोट-TOKEN-इथे")

@app.route('/')
def home():
    return "Bot is running"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id=chat_id, text="Hello! I'm Agentic AI.")
    return "OK"

if __name__ == '__main__':
    app.run()
