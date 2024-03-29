import logging
import threading
import time
import serial

from smartwebbot.boardfunctions import pencontroller
from smartwebbot.boardfunctions import engine


status = "IDLE"
thread = None
job = "NONE"
pen = "LOW"



class ExecutionThread(threading.Thread):
    def __init__(self, target, args):
        super().__init__(target=target, args=args)
        self.target = target
        self._kill = threading.Event()

    def kill(self):
        logging.basicConfig(level=logging.NOTSET)
        logging.info("Stopping action")
        if self.target.__name__ == "draw":
            engine.stopit()
        self._kill.set()


def getStatus():
    global status
    global thread
    global job
    global pen
    return status

def execute(task, *args):
    global status
    global thread
    global job
    global pen
    logging.basicConfig(level=logging.NOTSET)
    logging.info("Started job " + task.__name__)
    if status == "WORKING":
        cancel()
    status = "WORKING"

    if str(task) == "lowerPen":
        pen = "LOW"
    elif str(task) == "liftPen":
        pen = "HIGH"

    job = task.__name__
    thread = ExecutionThread(target=task, args=args)
    thread.start()

def cancel():
    global status
    global thread
    global job
    global pen
    if not thread:
        return

    if not thread.is_alive() and status == "WORKING":
        status = "FINISHED"
        return
    else:
        thread.kill()

    if pen == "LOW":
        pencontroller.liftPen()

    status = "CANCELED"


def getStatus():
    global status
    global thread
    global job
    global pen
    if not thread:
        return status

    if not thread.is_alive() and status == "WORKING":
        status = "FINISHED"

    return status

def getJob():
    global status
    global thread
    global job
    global pen
    return job


def getPen():
    global pen
    return pen

def setPen(value):
    global pen
    pen = value
