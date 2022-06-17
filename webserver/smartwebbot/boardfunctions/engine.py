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

def draw(scale, color, offsetx, offsety, path):
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Sending file " + path)
    
    logging.info("Opening Serial")
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    if(ser.isOpen() == False):
        ser.open()  
    ser.timeout = 1

    file = open(path, 'r')

    for i in range(0,5):
        answer = ser.readline().decode("UTF-8")
        logging.info("Got answer " + answer)


    ser.write(str.encode("G28 X;\n"))
    logging.info("Sending homing line: " + "G28 X;\n")
    answer = ser.readline().decode("UTF-8")
    logging.info("Got answer " + answer)
    answer = ser.readline().decode("UTF-8")
    while "processing" in answer:
        answer = ser.readline().decode("UTF-8") 
        logging.info("Got answer " + answer)
    time.sleep(3)
    ser.write(str.encode("G28 Y;\n"))
    logging.info("Sending homing line: " + "G28 Y;\n")
    answer = ser.readline().decode("UTF-8")
    logging.info("Got answer " + answer)
    while "processing" in answer:
        answer = ser.readline().decode("UTF-8") 
        logging.info("Got answer " + answer)
    time.sleep(3)

    dolanpsstop = False
    
    for line in file:
        global stopped
        if stopped:
            if color=="RED":
                line = "M42 P5 S240;\n"
            elif color=="BLUE":
                line = "M42 P4 S110;\n"
            if ser.isOpen():
                ser.write(str.encode(line))
                answer = ser.readline().decode("UTF-8")
                logging.info("Got answer " + answer)
            pencontroller.lowerPen()
            stopped = False
            return
        if "M5" in line:
            #time.sleep(3)
            pencontroller.liftPen()
            line = "M400;\n"
            ser.write(str.encode(line))

            answer = ser.readline().decode("UTF-8")
            logging.info("Got answer " + answer)

            if color=="RED":
                line = "M42 P5 S240;\n"
            elif color=="BLUE":
                line = "M42 P4 S110;\n"
            
        elif "M3" in line:
            #time.sleep(3)
            pencontroller.lowerPen()

            line = "M400;\n"
            ser.write(str.encode(line))
            answer = ser.readline().decode("UTF-8")
            logging.info("Got answer " + answer)

            #if dolanpsstop:
            #    time.sleep(5)
            #    dolanpsstop = False
            if color=="RED":
                line = "M42 P5 S110;\n"
            elif color=="BLUE":
                line = "M42 P4 S240;\n"
        elif "G1" in line:
            firstpart = line.split("X")[0]
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1]) + float("00" + offsetx)
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2]) + float("00" + offsety)
            line = firstpart + "X" + str(ycoord*float(scale)) + " Y" + str(50+xcoord*float(scale)) + ";\n"


        ser.write(str.encode(line))
        logging.info("Sent line " + line)

        answer = ser.readline().decode("UTF-8")
        logging.info("Got answer " + answer)
        if "G1" in line:
            while not "ok" in answer:
                answer = ser.readline().decode("UTF-8") 
                logging.info("Got answer " + answer)
        else:
            while "processing" in answer:
                answer = ser.readline().decode("UTF-8") 
                logging.info("Got answer " + answer)
        

        time.sleep(0.1)
    ser.write(str.encode("G28 X;\n"))
    logging.info("Sending homing line: " + "G28 X;\n")
    answer = ser.readline().decode("UTF-8")
    logging.info("Got answer " + answer)
    answer = ser.readline().decode("UTF-8")
    if "G1" in line:
        while not "ok" in answer:
            answer = ser.readline().decode("UTF-8") 
            logging.info("Got answer " + answer)
            time.sleep(0.1)
    else:
        while "processing" in answer:
            answer = ser.readline().decode("UTF-8") 
            logging.info("Got answer " + answer)
    time.sleep(3)
    ser.write(str.encode("G28 Y;\n"))
    logging.info("Sending homing line: " + "G28 Y;\n")
    answer = ser.readline().decode("UTF-8")
    logging.info("Got answer " + answer)
    while "processing" in answer:
        answer = ser.readline().decode("UTF-8") 
        logging.info("Got answer " + answer)
    time.sleep(3)
    ser.close()


def getNextSourceIndex():
    return getSourceIndex() + 1


def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/gcode/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "gcode" + str(i) + ".gcode"):
            return i - 1
    return -1
