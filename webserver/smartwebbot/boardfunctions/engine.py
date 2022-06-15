import os

import serial
import time
import logging

from smartwebbot.boardfunctions import pencontroller


def draw(offsetx, offsety, path):
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Sending file " + path)
    #ser = serial.Serial('/dev/ttyUSB0', 250000)
    file = open(path, 'r')

    for line in file:
        if "M5" in line:
            #time.sleep(3)
            pencontroller.liftPen()
            #time.sleep(3)
        elif "M3" in line:
            #time.sleep(3)
            pencontroller.lowerPen()
            #time.sleep(3)
        elif "G1" in line:
            firstpart = line.split("X")[0]
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1]) + float(offsetx)
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2]) + float(offsety)
            line = firstpart + "X" + str(xcoord) + " Y" + str(ycoord) + ";"


        #ser.write(str.encode(line))
        logging.info("Sent line " + line)

        time.sleep(1)
        continue
    #ser.close()


def getNextSourceIndex():
    return getSourceIndex() + 1


def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/gcode/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "gcode" + str(i) + ".gcode"):
            return i - 1
    return -1