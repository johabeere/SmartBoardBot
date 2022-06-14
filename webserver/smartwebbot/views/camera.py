from django.http import HttpResponse
from smartwebbot.boardfunctions import camera


def take_picture(request):
    camera.take_picture()
    return HttpResponse(200)
