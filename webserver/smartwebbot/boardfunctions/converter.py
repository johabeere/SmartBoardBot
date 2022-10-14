import string
import random

from smartwebbot import constants
import logging
import os
import subprocess

from smartwebbot.boardfunctions import hatched

from smartwebbot.models.Document import Document


def convert(user):
    logging.basicConfig(level=logging.NOTSET)

    myimg = Document.objects.filter(fileType=constants.JPEG).latest('created_on').data
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for i in range(20))
    file = open(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".jpg", "wb")
    file.write(myimg)
    file.close()
    hatched.hatch(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".jpg", hatch_pitch=5, levels=(20, 100, 180), blur_radius=1)
    Document.create(user, "hatched_jpg", open(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".svg", "rb").read(),
                    "SVG", )
    os.remove(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".jpg")
    os.remove(os.getcwd() + "/smartwebbot/tmp/" + random_name + ".svg")
