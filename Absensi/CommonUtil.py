from adafruit_platformdetect import Detector

def checkAdafruitBoard():
    detector = Detector()
    print("Chip id: ", detector.chip.id)
    print("Board id: ", detector.board.id)

    # Check for specific board models:
    print("Pi 3B+? ", detector.board.RASPBERRY_PI_3B_PLUS)
    print("BBB? ", detector.board.BEAGLEBONE_BLACK)
    print("Orange Pi PC? ", detector.board.ORANGE_PI_PC)
    print("generic Linux PC? ", detector.board.GENERIC_LINUX_PC)
