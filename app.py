  
#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

import requests
import sys
import os
import json

import logging

import pycurl
app = Flask(__name__)
ACCESS_TOKEN = 'EAAgFgSzOWVIBAKwKnznEQMhyZB3NJv241QFeOvJ0Er5RvLMfgBR85Cc6peGmCyLdtgMSYYg7964cDIruILaRuWpWGC9chF7nE1jvmTy5h5HZB2CBCRZBf9XXecrm7DmpvybCDXhLkqnZBqwoYp9s1Q3bZBzvKKVMBFczyjKw5e3lUUfBPmQXH'
VERIFY_TOKEN = 'cultivartec_token'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET','POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        print('intenó ???')
        # get whatever message a user sent the bot
        output = request.get_json()

        #encoded
        data_string = json.dumps(output)

        #Decoded
        decoded = json.loads(data_string)


        print ("type:"+ str(json.dumps(decoded)))
        print ("type:"+ str(json.dumps(decoded['entry'][0])))
        print ("type:"+ str(json.dumps(decoded['entry'][0]['changes'][0]['field'])))
        print ("item:"+ str(json.dumps(decoded['entry'][0]['changes'][0]['value']['item'])))
        print ("msg:"+ str(json.dumps(decoded['entry'][0]['changes'][0]['value']['message'])))
        #post_id
        #parent_id = json.dumps(decoded['entry'][0]['changes'][0]['value']['parent_id'])
        #id = json.dumps(decoded['entry'][0]['id'])
        #id= id.replace('"', '')
        #sender_id
        #id = json.dumps(decoded['entry'][0]['changes'][0]['value']['sender_id'])
        id = json.dumps(decoded['entry'][0]['id'])
        id= id.replace('"', '')
        object_id__ = json.dumps(decoded['object'])
        comend_id = json.dumps(decoded['entry'][0]['changes'][0]['value']['comment_id'])
        accss_token = 'EAAgFgSzOWVIBAKwKnznEQMhyZB3NJv241QFeOvJ0Er5RvLMfgBR85Cc6peGmCyLdtgMSYYg7964cDIruILaRuWpWGC9chF7nE1jvmTy5h5HZB2CBCRZBf9XXecrm7DmpvybCDXhLkqnZBqwoYp9s1Q3bZBzvKKVMBFczyjKw5e3lUUfBPmQXH'
        comend_id_ = comend_id.replace('"', '')

        object_id__ = object_id__.replace('"', '')
        print(id)

        reply = "Hi I am your virtual assitant, you can call me Brayan"
        #para responder comentarios
        #"&parent_comment_id="+parent_id+
        #+"&object_id="+id

    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()