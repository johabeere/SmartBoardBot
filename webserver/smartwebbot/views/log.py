import json

from django.http import HttpResponse, HttpResponseRedirect
from smartwebbot.boardfunctions import logger, engine
from django.shortcuts import render



#vars for getting logs:
def getlogs(request):
    text = logger.load_logs()
    #return render(request, "panels/connection/connection-log.html", {"text":text})
    return HttpResponse(text)
def applyFilters(request):
    logger.flags[0]=bool(request.POST.get('all')) ## enables Tracebacks and other Multifile Messages
    logger.flags[1]=bool(request.POST.get('debug'))
    logger.flags[2]=bool(request.POST.get('info'))
    logger.flags[3]=bool(request.POST.get('error'))
    logger.flags[4]=bool(request.POST.get('warning'))
    logger.flags[5]=bool(request.POST.get('critical'))
    logger.log(logger.flags, 30)
    return HttpResponse("200")
def clearlogs(request):
    logger.clear_logs();
    return HttpResponse("200");
def update_log(request):
    return HttpResponse(logger.check_new());

def send_gcode(request):
    engine.serialsend(str.encode(str(request.POST.get('gcode-input'))), True)
    logger.log("I got a gcode", 30)
    return HttpResponse("200")