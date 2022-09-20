from asyncio import constants
import logging
import os
import subprocess

from smartwebbot.boardfunctions import hatched

from smartwebbot.models.Document import Document


def convert(user):
    logging.basicConfig(level=logging.NOTSET)

    myimg = Document.objects.latest(fileType=constants.JPEG).data
    output = hatched.hatch(myimg, hatch_pitch=5, levels=(20,100,180),blur_radius=1)
    Document.create(user, "hatched_jpg",output,"SVG",)

    