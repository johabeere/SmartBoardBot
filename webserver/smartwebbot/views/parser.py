from django.http import HttpResponse
from smartwebbot.boardfunctions import parser
import os

def parse_file(request):
    parser.parse_svg(os.getcwd() + "/smartwebbot/static/svg/testfile.svg")
    return HttpResponse("200")