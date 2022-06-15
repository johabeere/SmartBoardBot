import logging

from smartwebbot.boardfunctions import boardcontroller


def lowerPen():
    boardcontroller.setPen("LOW")
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Lowering Pen")


def liftPen():
    boardcontroller.setPen("HIGH")
    logging.basicConfig(level=logging.NOTSET)  # Here
    logging.info("Lifting Pen")
    