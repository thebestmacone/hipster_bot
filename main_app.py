from flask import Flask
import telebot

TOKEN = "228729068:AAEGPXDTrOO42qhu00gDGp4Iu77m14EC8ew"
app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

@app.route("/")
def hello():
	return "Hello from Flask!"

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Yeap, Bro")

if __name__ == "__main__":
	app.run()
	bot.polling()
