#!/usr/bin/env python
import os

#from picamera import PiCamera
from time import sleep

def take_picture():
    #return ""
    #camera = PiCamera()
    #camera.start_preview()
    #sleep(5)
    path = os.getcwd() + "/smartwebbot/static/img/photos/image"+str(get_current_index() + 1)+".jpg"
    command = "libcamera-jpeg -o " + path
    os.system(command)
    #camera.capture(path)
    #camera.stop_preview()


def get_current_index():
    img_dir = os.getcwd() + "/smartwebbot/static/img/photos/"

    filename = "not_found"
    for i in range(0, 100000):
        if not os.path.exists(img_dir + "image" + str(i) + ".jpg"):
            return i-1
    return -1

def get_current_filename_web():
    index = get_current_index()
    if index != -1:
        return "/static/img/photos/image"+str(index)+".jpg"
    else:
        return "not found"
    
def get_current_filename():
    index = get_current_index()
    if index != -1:
        return os.getcwd() + "/smartwebbot/static/img/photos/image" + str(index) + ".jpg"
    else:
        return "not found"
