#!/bin/bash

# This is meant for setting up autostart, 
# feel free to use it for manual start as well if autostart isn't configured! ($ ./start.sh)
# ONLY WORKS AFTER INSTALL SCRIPT!!!!!!
# NEVER MOVE THIS FILE OR PARENT DIRECTORY!!!!
# NEVER MODIFY LINE NUMBERS!!!

d="/home/adolf/SmartBoardBot"
python /home/adolf/SmartBoardBot/webserver/manage.py runserver 0.0.0.0:8080