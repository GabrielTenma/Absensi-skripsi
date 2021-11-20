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
        print(image)
        data = {'suhu':temperature}
        files=[('file',('file.jpeg',open(image,'rb'),'image/jpeg'))]
        r = requests.post(url= util.endpointCall(appConfig.URL_FACE_RECOG), headers= appConfig.HEAD_BEARER, data=data, files=files)
        result = r.json()['success'] #return true/false
        util.collectLog("[POST] matchImagePerson: OK, " + result,util.Logstate.ERROR)
    except:
        util.collectLog("[POST] matchImagePerson: occured ",util.Logstate.ERROR)
        sys.exc_info()
        #print(traceback.format_exc())
    return result