import os
from time import sleep

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from SmartBoardBot.webserver.manage import getController
from SmartBoardBot.webserver.smartwebbot.boardfunctions import converter, parser, engine
from SmartBoardBot.webserver.smartwebbot.models.Document import Document
from SmartBoardBot.webserver.smartwebbot.models.Image import Image
from SmartBoardBot.webserver.smartwebbot.models.VectorGraphic import VectorGraphic

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


def start_drawing(request):
    controller = getController()

    file = request.FILES['file']
    if file.name.endsiwth('.jpg'):
        image = Image.create(request.user, file.name, file.read(), True)
        fs = FileSystemStorage(location = os.getcwd()+'/smartwebbot/static/jpg/')
        filename = fs.save(converter.getNextSourceIndex(), file)

        controller.execute(converter.convert, filename, os.getcwd() + "/smartwebbot/static/svg/svg" + converter.getNextTargetIndex())
        while controller.getStatus() == "WORKING":
            sleep(0.5)
        if controller.getStatus() != "FINISHED":
            return

    elif file.name.endswith('.svg'):
        vector = VectorGraphic.create(request.user, file.name, file.read(), True)
        fs = FileSystemStorage(location=os.getcwd() + '/smartwebbot/static/svg/')
        filename = fs.save(converter.getNextTargetIndex(), file)

    controller.execute(parser.parse, parser.getSourceIndex(), parser.getNextTargetIndex())
    while controller.getStatus() == "WORKING":
        sleep(0.5)
    if controller.getStatus != "FINISHED":
        return

    controller.execute(engine.draw, engine.getSourceIndex())

    return HttpResponse("200")


def start_scan(request):
    controller = getController()

    return HttpResponse("200")


def cancel_drawing(request):
    controller = getController()

    controller.cancel()

    return HttpResponse("200")


def cancel_scan(request):
    controller = getController()

    controller.cancel()

    return HttpResponse("200")


def update_dashboard(request):
    controller = getController()

    return HttpResponse({
        'status': controller.getStatus(),
        'job': controller.getJob()
    })
