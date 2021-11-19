import sys
from PIL import Image, ImageDraw, ImageFilter
import App.util.CommonUtil as util
import App.config.variable.ApplicationConstant as appConfig
import requests
import traceback


# Raw post
def rawPost(address, param, data):
    r = requests.post(url= appConfig.ENDPOINT_URL + address ,data= data)
    return r.json

# send image & receive person name :: POST
def matchImagePerson(temperature, image):
    result = ''
    try:
        data = {'suhu':temperature}
        files=[('file',('',open(image,'rb'),'image/png'))]
        print(image)
        r = requests.post(url= appConfig.ENDPOINT_URL + appConfig.URL_FACE_RECOG, headers= appConfig.HEAD_BEARER, data=data, files=files)
        result = r.json()['content']['nama']
    except:
        print('[POST] matchImagePerson Is ', sys.exc_info(), ' occured')
        #print(traceback.format_exc())
    return result

# example api
print(matchImagePerson('20',appConfig.TAKE_PICTURE_FILENAME))