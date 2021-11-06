import requests
import base64

# Api Endpoint
ENDPOINT_URL = "https://attendance-serviceku.herokuapp.com"

# Bearer Token
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN5YWhydWwiLCJpYXQiOjE2MzU1NzA4OTgsImV4cCI6MTYzNjQzNDg5OH0.OJsH1eAzamr1ap3oenwpmIktKIKHFwS_5ajX6XHh9iI"

# Custom Header
HEAD_BEARER = {"Authorization": "Bearer " + BEARER_TOKEN}

# Raw post
def rawPost(address, param, data):
    r = requests.post(url= ENDPOINT_URL + address ,data= data)
    # response result
    return r.json

# send image & receive person name :: POST
def matchImagePerson(temperature, image):
    encodedImage = base64.b64encode(image)
    dictData = {'suhu':temperature,
                'file':image}

    r = requests.post(url= ENDPOINT_URL + "/v1/image", data=dictData, headers= HEAD_BEARER)
    return r.json()['data']


