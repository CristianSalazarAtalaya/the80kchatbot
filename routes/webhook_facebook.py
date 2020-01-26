#Flask dependencies
from flask import Blueprint, request

#Project dependencies
from config.config import ConfigFacebook

#Blueprint
facebook_webhook = Blueprint('facebook_webhook', __name__)

facebook_config = ConfigFacebook()

@facebook_webhook.route("/webhooks/facebook/", methods=['GET','POST'])
def facebook_challenge():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        print("validacion token")
        return verify_fb_token(token_sent)
    else:
        print('intenó ???')


#@facebook_webhook.route("/webhooks/facebook/", methods=['POST'])
#accss_tokendef facebook_webhook():
#       print('intenó ???')

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == facebook_config.VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
