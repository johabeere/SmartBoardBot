import logging
import os
import subprocess

import svg_to_gcode
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode import UNITS
from svg_to_gcode.compiler import Compiler, interfaces
from SmartBoardBot.webserver.smartwebbot import constants
from smartwebbot.models.Document import Document


def parse(user, slicer):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Starting from svg to gcode with latest file from Database")

    # Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
    # how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
    #gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=0)

    myData=Document.objects.latest(fileType=constants.SVG).data
    
    if slicer == "OLD":
        logging.info("Using old slicer")
        gcode_compiler = Compiler(interfaces.Gcode, movement_speed=8000, cutting_speed=2000, pass_depth=0)

        curves = parse_file(myData) # Parse an svg file into geometric curves

        gcode_compiler.append_curves(curves)
        gcode_compiler.unit = "mm"
        Document.create(user, 'compiled gcode', gcode_compiler.compile(passes=1),'GCODE') 

    else:


        logging.info("LOOKOUT -> New Slicer not implemented yet")
        #output = subprocess.check_output(["python2.7", "svg2gcode/svg2gcode.py", myData, target])


    #generate_gcode(source, target)
    logging.info("Finished parsing.")

