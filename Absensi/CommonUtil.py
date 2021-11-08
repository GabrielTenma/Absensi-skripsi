from adafruit_platformdetect import Detector
import logging
import requests

def checkAdafruitBoard():
    detector = Detector()

    logging.info("------------------[Board Detector]------------------")
    print("Chip id: ", detector.chip.id)
    print("Board id: ", detector.board.id)
    # Check for specific board models:
    logging.info("Pi 3B+? ", detector.board.RASPBERRY_PI_3B_PLUS)
    logging.info("BBB? ", detector.board.BEAGLEBONE_BLACK)
    logging.info("Orange Pi PC? ", detector.board.ORANGE_PI_PC)
    logging.info("generic Linux PC? ", detector.board.GENERIC_LINUX_PC)
    logging.info("------------------------------------------------------")


# check http status response
def checkHttpStatus(request):
    if request.status_code == 200:
        return True
    else:
        return False
