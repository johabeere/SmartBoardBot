import logging
import os
import random
import string
import subprocess

import svg_to_gcode
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode import UNITS
from svg_to_gcode.compiler import Compiler, interfaces
from smartwebbot import constants
from smartwebbot.models.Document import Document


def parse(user, slicer):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Starting from svg to gcode with latest file from Database")

    # Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
    # how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
    #gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=0)

    myData=Document.objects.filter(fileType=constants.SVG).latest('created_on').data
    if slicer == "OLD":
        logging.info("Using old slicer")
        gcode_compiler = Compiler(interfaces.Gcode, movement_speed=2000, cutting_speed=2000, pass_depth=0)

        letters = string.ascii_lowercase
        random_name = ''.join(random.choice(letters) for i in range(20))
        file = open(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".svg", "wb")
        file.write(myData)
        file.close()

        # Refusing to write comments on code due to the 3 litres of beer the evening before
        curves = parse_file(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".svg") # Parse an svg file into geometric curves

        #os.remove(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".svg")

        gcode_compiler.append_curves(curves)
        gcode_compiler.unit = "mm"
        gcode_compiler.compile_to_file(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".gcode", passes=1)
        #logger.log(str.encode(gcode_compiler.compile(passes=1)))
        gcodefile = open(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".gcode", "r")
        
        Document.create(user, 'compiled gcode', str.encode(gcodefile.read()),'GCODE')
        logger.log("created db entry for\t" + random_name)
        gcodefile.close()

    else:


        logging.info("LOOKOUT -> New Slicer not implemented yet")
        #output = subprocess.check_output(["python2.7", "svg2gcode/svg2gcode.py", myData, target])


    #generate_gcode(source, target)
    logging.info("Finished parsing.")

