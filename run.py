#from apis.watson import MensajeResponse

from config.config import ConfigWatson
#mensaje = MensajeResponse("Hola tio")
#print(mensaje.text)taa

data = ConfigWatson()
print(data.url)