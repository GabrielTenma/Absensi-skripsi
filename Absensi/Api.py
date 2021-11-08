from PIL import Image, ImageDraw, ImageFilter
import CommonUtil
import requests
import sys
import traceback


# Api Endpoint
ENDPOINT_URL = "https://attendance-serviceku.herokuapp.com"

# Bearer Token
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN5YWhydWwiLCJpYXQiOjE2MzU1NzA4OTgsImV4cCI6MTYzNjQzNDg5OH0.OJsH1eAzamr1ap3oenwpmIktKIKHFwS_5ajX6XHh9iI"

# Custom Header
HEAD_BEARER = {'Authorization': 'Bearer ' + BEARER_TOKEN}

# Raw post
def rawPost(address, param, data):
    r = requests.post(url= ENDPOINT_URL + address ,data= data)
    # response result
    return r.json

# send image & receive person name :: POST
def matchImagePerson(temperature, image):
    
    result = ''
    try:
        data = {'suhu':temperature}
        files=[('file',('image.png',open(image,'rb'),'image/png'))]
        r = requests.post(url= ENDPOINT_URL + "/absen/check", headers= HEAD_BEARER, data=data, files=files)
        result = r.json()['content']['nama']

    except:
        print('[POST] matchImagePerson Is ', sys.exc_info(), ' occured')
        #print(traceback.format_exc())
    return result

# example api
print(matchImagePerson('20','sample-image\\sample1.jpeg'))

