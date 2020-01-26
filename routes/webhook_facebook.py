#Flask dependencies
from flask import Blueprint, request
import json
#Project dependencies
from config.config import ConfigFacebook

#Blueprint
facebook_webhook = Blueprint('facebook_webhook', __name__)

facebook_config = ConfigFacebook()


from pymessenger.bot import Bot



@facebook_webhook.route("/webhooks/facebook/", methods=['GET','POST'])
def facebook_challenge():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        print("validacion token")
        return verify_fb_token(token_sent)
    else:
        # get whatever message a user sent the bot
        print("intento")
        output = request.get_json()
        print(output)
        #output = request.get_json()
        #recipient_id = output["entry"]["uid"]
        print("output[entry][0]")
        dataentry = output["entry"][0]
        print("*************************entry*****")
        print(dataentry)
        print("*************************id*****")
        recipient_id=dataentry["messaging"][0]["sender"]["id"]
        print(recipient_id)
        print("*************************mensaje*****")
        print(recipient_id["messaging"][0]["message"]["text"])
        #encoded
        #data_string = json.dumps(output)
        bot = Bot(facebook_config.ACCESS_TOKEN)
        bot.send_text_message(recipient_id, "Rata")
        #print(data_string)
    return "Message Processed"



#@facebook_webhook.route("/webhooks/facebook/", methods=['POST'])
#accss_tokendef facebook_webhook():
#       print('intenó ???')

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == facebook_config.VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
