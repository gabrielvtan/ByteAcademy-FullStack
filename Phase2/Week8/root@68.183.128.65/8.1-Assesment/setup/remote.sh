#!/usr/bin/env bash

#dos2unix <file.sh> you need to do before exporting file

#TODO - Handle for operating systems that are not Ubuntu
apt-get -y update

# Install python3 package manager
apt-get -y install python3-pip

# Install `virtualenv`
pip3 install virtualenv

# Create the virtual environment
virtualenv -p python3 --no-site-packages run/lib 

#Activate `virtualenv`
source run/lib/bin/activate

# pip3 install flask - do this in virtualenv bc it is a dependency

# pip3 freeze > setup/requirements.txt - this saves a file with all the given dependencies

# Install Application dependencies
pip3 install -r setup/requirements.txt

pip3 install flask

# Install a firewall
apt-get -y install firewalld

# Enable the firewall if-and-when a power cycle occurs
systemctl enable firewalld

# Open a Port number permanently
firewall-cmd --add-port=5002/tcp --permanent

# Add HTTP as a service
firewall-cmd --add-service=http --permanent

# Update the firewall settings
systemctl reload firewalld

