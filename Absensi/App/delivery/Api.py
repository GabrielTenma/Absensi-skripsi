import sys
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
    nama = ''
    
    try:
        print(image)
        data = {'suhu':temperature}
        files=[('file',('file.jpeg',open(image,'rb'),'image/jpeg'))]
        r = requests.post(url= util.endpointCall(appConfig.URL_FACE_RECOG), verify=False, timeout=15, headers= appConfig.HEAD_BEARER, data=data, files=files)
        res = r.json()
        result = res['success'] #return true/false
        if(result):
            nama = res['obj']['nama']
        util.collectLog("[POST] matchImagePerson: OK, " + str(result) + str("\nname: " + nama),util.Logstate.INFO)
    except:
        util.collectLog("[POST] matchImagePerson: occured "+ str(sys.exc_info()),util.Logstate.INFO)
        #print(traceback.format_exc())
    return res