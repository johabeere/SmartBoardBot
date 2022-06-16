import os

from smartwebbot.boardfunctions import boardcontroller
import time
import logging
import serial
from smartwebbot.boardfunctions import pencontroller

stopped = False


def stopit():
    global stopped
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Stopping drawing")
    stopped = True

def draw(offsetx, offsety, path):
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Sending file " + path)
    
    logging.info("Opening Serial")
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    if(ser.isOpen() == False):
        ser.open()  
    ser.timeout = 1

    file = open(path, 'r')

    for line in file:
        global stopped
        if stopped:
            stopped = False
            return
        if "M5" in line:
            #time.sleep(3)
            pencontroller.liftPen()

            line = "M42 P4 S255;\n"
            line = ""
        elif "M3" in line:
            #time.sleep(3)
            pencontroller.lowerPen()

            line = "M42 P4 S0;\n"
            line = ""
        elif "G1" in line:
            firstpart = line.split("X")[0]
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1]) + float("00" + offsetx)
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2]) + float("00" + offsety)
            line = firstpart + "X" + str(xcoord) + " Y" + str(ycoord) + ";\n"


        ser.write(str.encode(line))
        logging.info("Sent line " + line)

        answer = ser.readline().decode("UTF-8")
        logging.info("Got answer " + answer)

        time.sleep(0.5)
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
