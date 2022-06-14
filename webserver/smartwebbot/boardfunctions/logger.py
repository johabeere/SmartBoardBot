#!/usr/bin/env python
import os

def load_logs():
    path = os.getcwd()+"/smartwebbot/static/logs/testlog.html"
    textfile=open(path)
    data = textfile.read()
    textfile.close()
    return data