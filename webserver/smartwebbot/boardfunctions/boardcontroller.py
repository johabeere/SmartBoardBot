import threading
import time

from SmartBoardBot.webserver.smartwebbot.boardfunctions import pencontroller


class Controller():
    def __init__(self):
        self.status = "IDLE"
        self.thread = None
        self.job = "NONE"
        self.pen = "LOW"

    def getStatus(self):
        return self.status

    def execute(self, task, *args):
        if self.status == "WORKING":
            self.cancel()
        self.status = "WORKING"

        if str(task) == "lowerPen":
            self.pen = "LOW"
        elif str(task) == "liftPen":
            self.pen = "HIGH"

        self.job = str(task)
        self.thread = threading.Thread(target=task, args=args)
        self.thread.start()

    def cancel(self):
        if not self.thread.is_alive():
            return False
        else:
            self.thread.terminate()

        if self.pen == "LOW":
            pencontroller.liftPen()

        self.status = "CANCELED"
        self.job = "NONE"

    def getStatus(self):
        if not self.thread.is_alive and self.status == "WORKING":
            self.status = "FINISHED"

        return self.status

    def getJob(self):
        return self.job