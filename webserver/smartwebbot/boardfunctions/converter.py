import logging
import os
import subprocess

from hatched import hatched


def convert(source, target):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Starting conversion of files: \n " + source + "\nto\n" + target)
    hatched.hatch(str(source), hatch_pitch=5, levels=(20,100,180),blur_radius=1)
    os.rename(source[:-3]+"svg",target) #DÖRING IST KEK
    #subprocess.run("mv", str(dir + source), "/home/adolf/SmartBoardB" )
    #os.replace(str(source[0:-3]+"svg"),str(os.getcwd()+"/smartwebbot/static/svg/"+source[24:-3]+"svg"))

def getNextSourceIndex():
    return getSourceIndex() + 1

def getNextTargetIndex():
    return getTargetIndex() + 1

def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/jpg/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "jpg" + str(i) + ".jpg"):
            return i - 1
    return -1

def getTargetIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/svg/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "svg" + str(i) + ".svg"):
            return i-1
    return -1