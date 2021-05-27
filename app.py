from flask import Flask
from bot import Bot

app = Flask(__name__)


@app.route("/")
@app.route("/startbot",methods=['GET'])
def createBot():
    bot = Bot("Saarbrücken",False)
