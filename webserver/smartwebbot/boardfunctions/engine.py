from asyncio import constants
from asyncore import file_wrapper
import os
from xml.dom.minidom import DocumentType

from django.conf import settings
from smartwebbot.models.Document import Document

import time
import logging
import serial
from smartwebbot.boardfunctions import pencontroller, logger

stopped = False

if settings.LIVE:
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    logger.log("Initialized serial port in LIVE mode")
else:
    logger.log("Not in LIVE mode - not sending data via USB")
    ser = None


def stopit():
    global stopped
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Stopping drawing")
    stopped = True


def serialsend(line, last=False):
    if settings.LIVE:
        if(ser.isOpen() == False):
            ser.open()
            logger.log("opening Serial now...")
        ser.timeout = 1

        ser.write(str.encode(line))
        if "G28" in line:
            logger.log("sending HOMING Signal: "+line)
        else:
            logger.log("send\t"+line+"\t to Controller." )

        answer = ser.readline().decode("UTF-8")
        while ("processing" in answer) or (not "ok" in answer):
            answer = ser.readline().decode("UTF-8")
            logging.info("Got answer " + answer)
        logger.log ("got answer:\t"+answer)
        if(last):
            ser.close()
            logger.log("closing Serial now....")
        return answer
    else:
        logging.basicConfig(level=logging.NOTSET)
        logging.info("[USB]: Would send line " + str(line))
        logger.log("[USB]: Would send line " + str(line))

def home():
    serialsend("G28 X;\n")
    time.sleep(3)
    serialsend("G28 Y;\n")
    logger.log("homed, bitch!")
    time.sleep(3)
    return 0

def draw(scale, color, offsetx, offsety):
    logger.log("Getting latest gcode from Database")    


    mydata = Document.objects.latest(fileType=constants.GCODE).data

    ##NO IDEA WHAT THE FOLLOWING THREE LINES DO; KEEPING THEM JUST IN CASE....
    #for i in range(0,5):
    #    answer = ser.readline().decode("UTF-8")
    #    logging.info("Got answer " + answer)


    home()

    for line in mydata:
        global stopped
        if stopped:
            if color=="RED":
                serialsend("M42 P5 S240;\n")
            elif color=="BLUE":
                serialsend("M42 P4 S110;\n")
            pencontroller.lowerPen()
            stopped = False
            return
        if "M5" in line:
            time.sleep(3)
            pencontroller.liftPen()
            serialsend("M400;\n")

            if color=="RED":
                serialsend("M42 P5 S240;\n")
            elif color=="BLUE":
                serialsend("M42 P4 S110;\n")
            
        elif "M3" in line:
            #time.sleep(3)
            pencontroller.lowerPen()

            serialsend("M400;\n")

            if color=="RED":
                serialsend("M42 P5 S110;\n")
            elif color=="BLUE":
                serialsend("M42 P4 S240;\n")
        
        elif "G1" in line:
            firstpart = line.split("X")[0]
            ###REMOVE THIS ABOMINATION!!!!###
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1]) + float("00" + offsetx)
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2]) + float("00" + offsety)
            line = firstpart + "X" + str(ycoord*float(scale)) + " Y" + str(50+xcoord*float(scale)) + ";\n"
            serialsend(line)
        
        else:
            #Catch any other Gcode (in Theory never called)
            serialsend(line)        

        time.sleep(0.1)
    
    ##Goodbye Message; Reports Current Position for Debugging
    serialsend("M114;\n", True)

