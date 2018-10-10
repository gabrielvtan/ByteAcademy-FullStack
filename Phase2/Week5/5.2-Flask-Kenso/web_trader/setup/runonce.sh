#!/usr/bin/env bash

# Note: You may have to run the following script
#       as an administrative user by prepending
#       commands that draw `permission denied`
#       errors with `sudo `.

# Install `pip3`
apt-get -y install python3-pip

# Install `virtualenv`
pip3 install virtualenv

# Create a virtual environment
virtualenv -p python3 --no-site-packages run/lib

# Activate the virtual environment
source run/lib/bin/activate

# Install dependencies
pip3 install -r setup/requirements.txt

