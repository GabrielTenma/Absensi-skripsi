import sys
import time

# Variables
thermalMaxTemp = 0.0                                    # thermal maximum temp variable (thermalMaxTemp <- thermalDetectValue())
isDetectFace = False                                    # boolean val is steady detect face (isDetectValue <- VideoThread)
faceDetectedCount = 0                                   # detected face count

# Load
#sensorTc = I2CDevice(i2c, 0x69)
