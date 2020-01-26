from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#Configuracion
import json
#Recursos locales
from config.config import ConfigWatson

watson = ConfigWatson()

authenticator = IAMAuthenticator(watson.autenticator)
assistant = AssistantV1(
    version= watson.version,
    authenticator=authenticator
)
assistant.set_service_url(watson.url)

class MensajeResponse:

    def __init__(self, mensaje):
        self.mensaje = mensaje
        response = assistant.message(workspace_id=watson.workspaceid, input={'text': mensaje}).get_result()
        self.response = response
        self.text = response["output"]["text"][0]
        #r#eturn {'text' : response["output"]["text"][0] }

#mensaje = MensajeResponse("Hola tio")
#print(mensaje.text)

