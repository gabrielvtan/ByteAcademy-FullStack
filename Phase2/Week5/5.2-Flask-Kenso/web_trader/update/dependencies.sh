#!/usr/bin/env bash

# Note: You may have to run the following script
#       as an administrative user by prepending
#       commands that draw `permission denied`
#       errors with `sudo `.

# Activate the virtual environment
source run/lib/bin/activate

# Log dependencies
pip3 freeze > setup/requirements.txt
