from asyncore import file_wrapper
import os
from xml.dom.minidom import DocumentType

from django.conf import settings
from smartwebbot.models.Document import Document
from smartwebbot import constants

import time
import logging
import serial
import random
import string
from smartwebbot.boardfunctions import pencontroller, logger

stopped = False

if settings.LIVE:
    ser = serial.Serial('/dev/ttyUSB0', 250000)
    logger.log("Initialized serial port in LIVE mode")
else:
    logger.log("Not in LIVE mode - not sending data via USB")
    ser = None
if settings.FAKEGCODE:
    letters = string.ascii_lowercase
    file = open(os.getcwd()+"/smartwebbot/static/gcode/"+"TGC"+''.join(random.choice(letters) for i in range(5)) + ".gcode", "w")

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
            logger.log("sending\t"+line+"\t to Controller." )

        answer = ser.readline().decode("UTF-8")
        
        
        if "G1" in line:
            while (not "ok" in answer):
                logging.info("Got answer: " + answer)
                answer=ser.readline().decode("UTF-8")
        elif ("M3" or "M5" in answer):
            logger.log("proceeding after MCode....")
        
        else:  
             while (answer!=""):
                 logging.info("Got answer: " + answer)
                 answer = ser.readline().decode("UTF-8")
             time.sleep(0.1)
        #while ("processing" in answer) or ("busy" in answer):
        #    answer = ser.readline().decode("UTF-8")
        #    logging.info("Got answer " + answer)
        #logger.log ("got answer:\t"+answer)
        if(last):
            ser.close()
            logger.log("closing Serial now....")
        return answer
    else:
        logging.basicConfig(level=logging.NOTSET)
        logger.log("[USB]: Would send line " + str(line), 20)
        if settings.FAKEGCODE:
            file.write(str(line) + '\n')
            if(last):
                file.close()
                logger.log("closing Fake-GCode now....")

def home():
    #pencontroller.lowerPen()
    #serialsend("M400;\n")
    serialsend("M280 P1 S90;\n")
    serialsend("M280 P2 S95;\n")
    
    serialsend("G28 X;\n")
    time.sleep(3)
    serialsend("G28 Y;\n")
    logger.log("homed, bitch!")
    time.sleep(3)
    return 0

def draw(scale, color, offsetx, offsety):
    logger.log("Getting latest gcode from Database")    


    mydata = Document.objects.filter(fileType=constants.GCODE).latest('id').data.decode("UTF-8")
    #logger.log(mydata)
    ##NO IDEA WHAT THE FOLLOWING THREE LINES DO; KEEPING THEM JUST IN CASE....
    #for i in range(0,5):
    #    answer = ser.readline().decode("UTF-8")
    #    logging.info("Got answer " + answer)


    home()

    minx = float("inf")
    miny = float("inf")
    maxx = float("-inf")
    maxy = float("-inf")
    for line in mydata.split("\n"):
        if "G1" in line:
            # line.split("X") returns {"G1 "}{"123 Y456;\n"}
            # (line.split("X")[1]).split("Y") returns {"123 "} {"456;\n"}
            # (line.split("X")[1]).split("Y")[0] returns {"123 "}
            # (line.split("X")[1]).split("Y")[0][:-1] returns {"123"} (cuts the last character)
            # + float("00" + offsetx) is obvious.
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1])

            # line.split("X") returns {"G1 "}{"123 Y456;\n"}
            # (line.split("X")[1]).split("Y") returns {"123 "} {"456;\n"}
            # (line.split("X")[1]).split("Y")[1] returns {"123;\n"}
            # (line.split("X")[1]).split("Y")[0][:-2] returns {"123"} (cuts the last two characters)
            # + float("00" + offsety) is obvious.
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2])

            if xcoord < minx:
                minx = xcoord
            if ycoord < miny:
                miny = ycoord

            if xcoord > maxx:
                maxx = xcoord
            if ycoord > maxy:
                maxy = ycoord

    print(maxy)
    print(maxx)

    print(scale)
    print(float(scale))

    #if float(maxy)*float(scale) > settings.TABLE_HEIGHT:
    #    raise ValueError("Image too tall!")
    #if float(maxx)*float(scale) > settings.TABLE_WIDTH:
    #    raise ValueError("Image too wide!")

    diffx = float(offsetx) - minx*float(scale)
    diffy = float(offsety) - miny*float(scale)

    width = float(scale) * (maxx - minx)
    height = float(scale) * (maxy - miny)

    logging.info("Processed coordinates:\n Max X|Y: " + str(maxx) + "|" + str(maxy) + "\n Diff X|Y: " + str(diffx) + "|"+
                 str(diffy) + "\n Width|Height: " + str(width) + "|" + str(height))

    for line in mydata.split("\n"):
        global stopped
        if stopped:
            if color=="RED":
                serialsend("M280 P1 S60;\n")
            elif color=="BLUE":
                serialsend("M280 P2 S20;\n")
            pencontroller.lowerPen()
            stopped = False
            return
        if "M3" in line:
            #time.sleep(3)
            pencontroller.liftPen()
            serialsend("M400;\n")

            if color=="RED":
                serialsend("M280 P1 S60\n")
            elif color=="BLUE":
                serialsend("M280 P2 S20;\n")
            
        elif "M5" in line:
            #time.sleep(3)
            pencontroller.lowerPen()

            serialsend("M400;\n")

            if color=="RED":
                serialsend("M280 P1 S90;\n")
            elif color=="BLUE":
                serialsend("M280 P2 S95;\n")
        
        elif "G1" in line:
            # returns "G1 "
            firstpart = line.split("X")[0]

            ###REMOVE THIS ABOMINATION!!!!###
            #logger.log("Offsets are: "+ offsetx+";"+offsety+" , Scale is: "+str(float(scale)))
            xcoord = float((line.split("X")[1]).split("Y")[0][:-1])*float(scale) + diffx

            #xcoord = float((line.split("X")[1]).split("Y")[0][:-1])  
            
            #ycoord = float((line.split("X")[1]).split("Y")[1][:-2])  
            ycoord = float((line.split("X")[1]).split("Y")[1][:-2])*float(scale) + diffy

            #logger.log("Coords are: ("+str(xcoord)+";"+str(ycoord)+")")
            #line = firstpart + "X" + str(ycoord*float(scale)+ float("00" + offsety)) + " Y" + str(xcoord*float(scale)+float("00"+offsetx)) + ";\n"
            line = firstpart + "X" + str(ycoord) + " Y" + str(xcoord) + ";\n"
            #logger.log("Xcord;\t"+xcoord +"Ycord;\t" + ycoord)
            serialsend(line)
        
        else:
            #Catch any other Gcode (in Theory never called)
            serialsend(line)        

        #time.sleep(0.1)
    serialsend("G1 X20 Y20;\n")
    ##Goodbye Message; Reports Current Position for Debugging
    serialsend("M114;\n", True)

