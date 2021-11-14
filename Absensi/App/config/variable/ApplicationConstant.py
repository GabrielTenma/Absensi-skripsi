import sys

# -- NOTE --
# for filepath use '/' for linux & '\\' for windows.

# APPLICATION CONFIGURATION
CAMERA_INDEX = 0                                                     # camera webcam index (default is 0)
CAMERA_FPS = 25                                                      # camera fps max limit
FILE_CASCADE = 'App/assets/haarcascade_frontalface_default.xml'      # cascade file location
LOG_FILENAME = 'verbose.log'                                         # log filename
TAKE_PICTURE_FILENAME = 'App/assets/photoshoot-user.jpg'             # take picture filename

# API CONFIGURATION
ENDPOINT_URL = "https://attendance-serviceku.herokuapp.com/"
BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InN5YWhydWwiLCJpYXQiOjE2MzU1NzA4OTgsImV4cCI6MTYzNjQzNDg5OH0.OJsH1eAzamr1ap3oenwpmIktKIKHFwS_5ajX6XHh9iI"
HEAD_BEARER = {'Authorization': 'Bearer ' + BEARER_TOKEN}

URL_FACE_RECOG = "absen/check"