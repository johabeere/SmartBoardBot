import os


def convert(source, target):
    None

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