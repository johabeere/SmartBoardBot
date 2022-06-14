from django.http import HttpResponse
from smartwebbot.getlogs import getlogs


def take_picture(request):
    getlogs.load_logs()
    return HttpResponse(200)
