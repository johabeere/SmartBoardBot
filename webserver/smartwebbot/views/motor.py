import os

from smartwebbot.boardfunctions import engine
from django.http import HttpResponse


def start_motor(request):
    engine.write_file(os.getcwd() + "/smartwebbot/static/gcode/testfile.gcode")
    return HttpResponse("200")