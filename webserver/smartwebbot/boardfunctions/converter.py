import logging
import os

import aspose.words as aw


def convert(source, target):
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Starting conversion of files: \n " + source + "\nto\n" + target)

    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(source)

    pageSetup = builder.page_setup
    pageSetup.page_width = shape.width
    pageSetup.page_height = shape.height
    pageSetup.top_margin = 0
    pageSetup.left_margin = 0
    pageSetup.bottom_margin = 0
    pageSetup.right_margin = 0

    doc.save(target)



def getNextSourceIndex():
    return getSourceIndex() + 1

def getNextTargetIndex():
    return getTargetIndex() + 1

def getSourceIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/jpg/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "jpg" + str(i) + ".jpg"):
            return i - 1
    return -1

def getTargetIndex():
    img_dir = os.getcwd() + "/smartwebbot/static/svg/"

    for i in range(0, 100000):
        if not os.path.exists(img_dir + "svg" + str(i) + ".svg"):
            return i-1
    return -1