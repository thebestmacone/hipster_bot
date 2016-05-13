import telebot 
import config 
import os 
from flask import Flask, request 

bot = telebot.TeleBot(config.TOKEN) 
app = Flask(__name__) 

@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.chat.id, 'Hello') 

@app.route("/bot", methods=['POST']) 
def getMessage(): 
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message]) 
    return "!", 200 

@app.route("/") 
def webhook(): 
    bot.remove_webhook() 
    bot.set_webhook(url="https://hipstertestbot.herokuapp.com/bot") 
    return "!", 200 

port = int(os.environ.get("PORT", 443)) 
app.run(host='0.0.0.0', port=port) 
