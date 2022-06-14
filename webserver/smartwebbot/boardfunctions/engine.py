import os

import serial
import time
import logging


def draw(path):
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Sending file " + path)
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    file = open(path, 'r')

    for line in file:
        ser.write(str.encode(line))
        logging.info("Sent line " + line)
        time.sleep(1)
        continue
    ser.close()


def getNextSourceIndex():
    return getSourceIndex() + 1


def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/gcode/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "gcode" + str(i) + ".gcode"):
            return i - 1
    return -1