from flask import Flask
# import bot_app

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello from Flask!"

if __name__ == "__main__":
	app.run()
	# bot_app.bot.polling()
