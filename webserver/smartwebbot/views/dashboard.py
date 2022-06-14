import json
import logging
import os
import threading
from concurrent.futures import thread
from time import sleep

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

from smartwebbot.boardfunctions import converter, parser, engine
from smartwebbot.models.Document import Document
from smartwebbot.models.Image import Image
from smartwebbot.models.VectorGraphic import VectorGraphic
from smartwebbot.boardfunctions import boardcontroller as controller

IDLE = 0

ERROR = -1

UPLOADING = 101
CONVERTING = 102
PARSING = 103
PAINTING = 104
DONE_DRAWING = 105

PHOTOGRAPHING = 201
STITCHING = 202
DONE_SCAN = 203

def start_drawing_handler(request):
    t1 = threading.Thread(target=start_drawing, args=[request])
    t1.start()
    return render(request, 'core/home.html')

def start_drawing(request):
    file = request.FILES['file']
    if file.name.endswith('.jpg'):
        fs = FileSystemStorage(location = os.getcwd()+'/smartwebbot/static/jpg/')
        filename = fs.save(os.getcwd() + "/smartwebbot/static/jpg/jpg" + str(converter.getNextSourceIndex())+".jpg", file)

        controller.execute(converter.convert, os.getcwd() + "/smartwebbot/static/jpg/jpg" + str(converter.getSourceIndex())+".jpg", os.getcwd() + "/smartwebbot/static/svg/svg" + str(converter.getNextTargetIndex()) + ".svg")
        while controller.getStatus() == "WORKING":
            sleep(0.5)
        if controller.getStatus() != "FINISHED":
            return HttpResponse("200")

    elif file.name.endswith('.svg'):
        fs = FileSystemStorage(location=os.getcwd() + '/smartwebbot/static/svg/')
        filename = fs.save(os.getcwd() + "/smartwebbot/static/svg/svg" + str(converter.getNextTargetIndex()) + ".svg", file)

    controller.execute(parser.parse, os.getcwd() + "/smartwebbot/static/svg/svg" + str(parser.getSourceIndex()) + ".svg", os.getcwd() + "/smartwebbot/static/gcode/gcode" + str(parser.getNextTargetIndex()) + ".gcode")
    while controller.getStatus() == "WORKING":
        sleep(0.5)
    if controller.getStatus != "FINISHED":
        return HttpResponse("200")

    controller.execute(engine.draw, os.getcwd() + "/smartwebbot/static/gcode/gcode" + str(engine.getSourceIndex()) + ".gcode")

    return HttpResponse("200")


def start_scan(request):
    controller = getController()

    return HttpResponse("200")


def cancel_drawing(request):
    controller.cancel()
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Drawing canceled")

    return HttpResponse("200")


def cancel_scan(request):

    controller.cancel()
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Scan canceled")

    return HttpResponse("200")


def update_dashboard(request):
    return HttpResponse(json.dumps({
        'status': controller.getStatus(),
        'job': controller.getJob()
    }))
