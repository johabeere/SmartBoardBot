import logging
import os

import svg_to_gcode
from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode import UNITS
from svg_to_gcode.compiler import Compiler, interfaces

def parse(source, target):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Starting parsing of files: \n " + source + "\nto\n" + target)

    # Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
    # how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=8000, cutting_speed=2000, pass_depth=0)

    curves = parse_file(source) # Parse an svg file into geometric curves

    gcode_compiler.append_curves(curves)
    gcode_compiler.unit = "mm"
    gcode_compiler.compile_to_file(target, passes=1)
    logging.info("Finished parsing.")

def getNextSourceIndex():
    return getSourceIndex() + 1

def getNextTargetIndex():
    return getTargetIndex() + 1

def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/svg/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "svg" + str(i) + ".svg"):
            return i - 1
    return -1

def getTargetIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/gcode/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "gcode" + str(i) + ".gcode"):
            return i-1
    return -1