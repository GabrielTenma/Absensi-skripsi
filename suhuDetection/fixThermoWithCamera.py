import time
import numpy as np
import cv2 as cv

import busio
import board

import adafruit_amg88xx

# deteksi port i2c kamera thermal
i2c = busio.I2C(board.SCL, board.SDA)
# initial sensor amg8833g
sensor = adafruit_amg88xx.AMG88XX(i2c)

time.sleep(0.2)

# camera normal input
cap = cv.VideoCapture(0)

# initial klasifikasi wajah
faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # untuk memisahkan ret dan frame
    ret, fram = cap.read()
    # frame rotate untuk memutar 90 derajat
    frame = cv.rotate(fram, cv.ROTATE_90_CLOCKWISE)
    h, w, c = frame.shape

    # mengubah gambar jadi abu abu
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #frame = cv.rotate(fram, cv.ROTATE_90_CLOCKWISE)
    # face detection menggunakan standard face cascade
    facerect = faceCascade.detectMultiScale(gray, scaleFactor=1.5 , minNeighbors=6, minSize=(1, 1))

    if len(facerect) > 0:
        for rect in facerect:
            cv.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 255, 0), thickness=2)
        
        max_temp = 0.0
        # susunan pixel dari thermal 8x8
        #
        pixels = sensor.pixels
        for x in range(len(pixels)):
            for y in range(len(pixels[0])):
                # simpan suhu maksimal
                if (pixels[x][y] > max_temp):
                    max_temp = pixels[x][y]
                
        print('SUHU Maksimal Terdeteksi pada camera thermal: '+str(max_temp))
        # ambil gambar encode ke byte64


    cv.imshow('camera capture', frame)

    # ESC
    if cv.waitKey(1) == 27:
        break

cap.release()
# close window
cv.destroyAllWindows()

