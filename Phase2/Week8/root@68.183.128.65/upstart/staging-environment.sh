#!/usr/bin/env bash

source run/lib/bin/activate 

# this allows you to run the application regardless if your computer is off
nohup python3 run/wsgi.py &
