from django.http import HttpResponse
from smartwebbot.boardfunctions import logger
from django.shortcuts import render


def getlogs(request):
    text = logger.load_logs()
    #return render(request, "panels/connection/connection-log.html", {"text":text})
    return HttpResponse(text)