import requests

# api endpoint
ENDPOINT_URL = "https://127.0.0.1/endpoint"


class Api():
    def Post(data):
        r = requests.post(url= ENDPOINT_URL,data= data)
        return r.text #response
