  
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
ACCESS_TOKEN = 'EAAJySaEbwKQBALarjyjb9hNQiCn6QNv7aM2XtfTUvxa5d3NmuieQ3TUwa01bkW3w0RyGID3t9gGyTYyQwHuTkhzJh7tdiZAuVhwZBrcEF5LRXqDlImhVZAgkyo9jmCThrjHPUxSanvLvbs4MsKheVI5zZAl1pimOHDqSIWXyTAeHMGWA5K5uZA3MDGvvOCR9SuqljPb8GzgZDZD'
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
        parent_id = json.dumps(decoded['entry'][0]['changes'][0]['value']['parent_id'])
        #id = json.dumps(decoded['entry'][0]['id'])
        #id= id.replace('"', '')
        #sender_id
        #id = json.dumps(decoded['entry'][0]['changes'][0]['value']['sender_id'])
        id = json.dumps(decoded['entry'][0]['id'])
        id= id.replace('"', '')
        object_id__ = json.dumps(decoded['object'])
        comend_id = json.dumps(decoded['entry'][0]['changes'][0]['value']['comment_id'])
        accss_token = 'EAAJySaEbwKQBAMzOcPemwC0NDPSwin01waSsnOetOU1Tc8nIjPlLZBAeg2BVNAGycSS5it2JQu7H3vTfKMZC5aOROKShoLgfZCmlZCsE7oEZAioCd2vw8em9PM1oIvYraoXbwjWpV2ab3pJDiYdT5hPP6iEFJELCExudjB6C89bWKhZBtK4VBSLnxVVWu24aTmXsJgVwD4LAZDZD'
        comend_id_ = comend_id.replace('"', '')

        object_id__ = object_id__.replace('"', '')
        print(id)

        reply = "Hi I am your virtual assitant, you can call me Brayan"
        #para responder comentarios
        #"&parent_comment_id="+parent_id+
        #+"&object_id="+id

        #+"&id="+id
        c = pycurl.Curl()
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        #c.setopt(pycurl.RETURNTRANSFER, 1)
        c.setopt(pycurl.POSTFIELDS, "message="+reply+"&id="+comend_id_+"&access_token="+accss_token)
        c.setopt(pycurl.URL, "https://graph.facebook.com/v3.3/comments/"+comend_id)
        c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        c.perform()
        print(c.getinfo_raw(pycurl.HTTP_CODE))


        """ para responder comentarios por mensaje privado
        c = pycurl.Curl()
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        #c.setopt(pycurl.RETURNTRANSFER, 1)
        c.setopt(pycurl.POSTFIELDS, "message="+reply +"&access_token="+accss_token)
        c.setopt(pycurl.URL, "https://graph.facebook.com/v3.3/"+comend_id+"/private_replies")
        c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        c.perform()
        print(c.getinfo_raw(pycurl.HTTP_CODE))
        """


        """
        import StringIO
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.perform()
        c.close()
        data = b.getvalue()
        """
        
        #c.setopt(pycurl.HTTPHEADER, ["Accept:"])
        #c.perform()
        #print(c.getinfo_raw(pycurl.HTTP_CODE))
        """
        CURLINFO_FILETIME is mapped as pycurl.INFO_FILETIME
        CURLINFO_COOKIELIST is mapped as pycurl.INFO_COOKIELIST
        CURLINFO_CERTINFO is mapped as pycurl.INFO_CERTINFO
        CURLINFO_RTSP_CLIENT_CSEQ is mapped as pycurl.INFO_RTSP_CLIENT_CSEQ
        CURLINFO_RTSP_CSEQ_RECV is mapped as pycurl.INFO_RTSP_CSEQ_RECV
        CURLINFO_RTSP_SERVER_CSEQ is mapped as pycurl.INFO_RTSP_SERVER_CSEQ
        CURLINFO_RTSP_SESSION_ID is mapped as pycurl.INFO_RTSP_SESSION_ID
        """


        """
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "message=$reply&access_token=$accessToken");
        curl_setopt($ch, CURLOPT_URL, "https://graph.facebook.com/v2.10/$commentID/private_replies");
        curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36");
        $response = curl_exec($ch);
        curl_close($ch);
        """



        c = pycurl.Curl()
        c.setopt(pycurl.URL, "http://www.python.org/")
        c.setopt(pycurl.HTTPHEADER, ["Accept:"])


        #bot_r = Bot(accss_token)
        #bot_r.send_text_message('100001133802215', reply)
        

        """
        decoded = json.loads(output)
        print(decoded['entry'][0])
        y = json.dumps(output['entry'][0]['changes']['id'])
        #y = json.dumps(output)
        print(y)
        """
        #logging.warning(output['object'])
  

        #archivo = open('texto.txt','a')
        #archivo.write(json.dumps(output['object']))
        #print(request)

        #logging.warning('msg')
        #print(output['object']['data'])
        """for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
                    """
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