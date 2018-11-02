#!/usr/bin/env bash

#Activate the virtual environment
source run/lib/bin/activate 

# Catalog application dependencies
pip3 freeze > setup/requirements.txt