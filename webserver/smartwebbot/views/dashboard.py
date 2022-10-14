from asyncio import constants
import json
import logging
import os
import threading
import serial
from concurrent.futures import thread
from time import sleep

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
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
    file = request.FILES['file']
    if file.name.endswith('.jpg') or file.name.endswith('.jpeg'):
        Document.create(request.user, "Uploaded_JPG", file.read(), "JPEG", True)
        t1 = threading.Thread(target=start_drawing_convert_img, args=[request])
        t1.start()
    elif file.name.endswith('.svg'):
        Document.create(request.user, "Uploaded_SVG", file.read(), "SVG", True)
        t1 = threading.Thread(target=start_drawing, args=[request])
        t1.start()
    # sleep(0.1)
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Returning Http Answer")

    return HttpResponseRedirect("/home")


def start_drawing_convert_img(request):
    controller.execute(converter.convert, request.user)
    while controller.getStatus() == "WORKING":
        sleep(0.5)
    if controller.getStatus() != "FINISHED":
        return HttpResponse("200")
    start_drawing(request)


def start_drawing(request):
    slicer = request.POST.get('slicer')

    controller.execute(parser.parse, request.user, slicer)
    while controller.getStatus() == "WORKING":
        sleep(0.5)
    if controller.getStatus() != "FINISHED":
        return HttpResponse("200")

    logging.info("Starting to draw image.")

    offsetx = request.POST.get('x-start')
    offsety = request.POST.get('y-start')

    scale = request.POST.get('scale')
    if scale == "":
        scale = "1"

    color = request.POST.get('color')

    sleep(0.1)

    controller.execute(engine.draw, scale, color, offsetx, offsety)

    return HttpResponse("200")


def start_scan(request):
    return HttpResponse("200")


def cancel_drawing(request):
    controller.cancel()
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Drawing canceled by viewer")

    return HttpResponse("200")


def cancel_scan(request):
    controller.cancel()
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Scan canceled")

    return HttpResponse("200")


def update_dashboard(request):
    return HttpResponse(json.dumps({
        'status': controller.getStatus(),
        'job': controller.getJob(),
        'pen': controller.getPen()
    }))
