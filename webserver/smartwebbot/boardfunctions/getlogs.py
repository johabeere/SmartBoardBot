#!/usr/bin/env python
import os

def load_log(index):
    path = os.getcwd()+"/smartwebbot/static/log/log"+index+".txt"
    textfile=open(path)
    data = textfile.read()
    textfile.close()
    return data