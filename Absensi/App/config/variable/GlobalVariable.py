import sys
import time
import busio
import board
import adafruit_amg88xx

# Variables
thermalMaxTemp = 0.0                                    # thermal maximum temp variable (thermalMaxTemp <- thermalDetectValue())
isDetectFace = False                                    # boolean val is steady detect face (isDetectValue <- VideoThread)
faceDetectedCount = 0                                   # detected face count

# Load
i2c = busio.I2C(board.SCL, board.SDA)                   # init board raspberry
sensorTc = adafruit_amg88xx.AMG88XX(i2c)                # init sensor AMG8833g
#sensorTc = I2CDevice(i2c, 0x69)
#time.sleep(3)                                           # need delay for read board io
