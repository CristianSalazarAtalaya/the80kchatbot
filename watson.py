from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

authenticator = IAMAuthenticator('xTGv8CzUcIF7Jj08W8Ui5n8HJ9Ilv7O4MVVmXcnPkOAL')
assistant = AssistantV1(
    version='2019-02-28',
    authenticator=authenticator
)

assistant.set_service_url('https://gateway.watsonplatform.net/assistant/api')

response = assistant.message(workspace_id='6dae5464-8ffe-4702-b7a9-35091af6ad5b', input={
    'text': 'Hola tio'}).get_result()
#print(json.dumps(response, indent=2)["output"]["text"][0]))
print(response["output"]["text"][0])