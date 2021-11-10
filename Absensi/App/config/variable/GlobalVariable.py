import sys
import time

# board lib
import busio
import board

# adafruit board lib
import adafruit_amg88xx



# Variables
thermalMaxTemp = 0.0                                    # thermal maximum temp variable (thermalMaxTemp <- thermalDetectValue())
isDetectFace = False                                    # boolean val is steady detect face (isDetectValue <- VideoThread)


i2c = busio.I2C(board.SCL, board.SDA)                   # init board raspberry
sensorTc = adafruit_amg88xx.AMG88XX(i2c)                # init sensor AMG8833g
time.sleep(1)                                           # need delay for read board io