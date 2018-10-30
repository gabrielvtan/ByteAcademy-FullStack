#!/usr/bin/env bash

# This sets ups the virtual environment
virtualenv -p python3 --no-site-packages run/lib 

source run/lib/bin/activate

# pip3 install flask - do this in virtualenv bc it is a dependency

# pip3 freeze > setup/requirements.txt - this saves a file with all the given dependencies

pip3 install -r setup/requirements.txt