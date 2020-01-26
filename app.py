  
#Python libraries that we need to import for our bot
from flask import Flask, request
from pymessenger.bot import Bot

#local resources
from routes.webhooks import simple_templates



import logging

app = Flask(__name__)

app.register_blueprint(simple_templates)

if __name__ == "__main__":
    #app.run(host="0.0.0.0",port=80)
    app.run()

