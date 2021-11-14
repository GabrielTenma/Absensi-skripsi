from adafruit_platformdetect import Detector
import logging
import requests
import os.path
from enum import Enum
import App.config.variable.ApplicationConstant as appConfig


# Initializer
logging.basicConfig()

class Logstate(Enum):
    INFO = 0
    ERROR = 1
    DEBUG = 2

def checkAdafruitBoard():
    detector = Detector()

    logging.info("------------------[Board Detector]------------------")
    logging.info("Chip id: " + str(detector.chip.id))
    logging.info("Board id: " + str(detector.board.id))

    # Check for specific board models:
    logging.info("Pi 3B+? " + str(detector.board.RASPBERRY_PI_3B_PLUS))
    logging.info("BBB? " + str(detector.board.BEAGLEBONE_BLACK))
    logging.info("Orange Pi PC? " + str(detector.board.ORANGE_PI_PC))
    logging.info("generic Linux PC? " + str(detector.board.GENERIC_LINUX_PC))
    logging.info("------------------------------------------------------")


# check http status response
def checkHttpStatus(request):
    if request.status_code == 200:
        return True
    else:
        return False

# check file is exist
def checkFileIsExist(filePath):
    if(os.path.isfile(filePath)):
        return True
    else:
        return False

# collect log
def collectLog(message,state):
    return {
        Logstate.INFO : logging.info(str(message)),
        Logstate.ERROR : logging.error(str(message)),
        Logstate.DEBUG : logging.debug(str(message))
    }[state]
