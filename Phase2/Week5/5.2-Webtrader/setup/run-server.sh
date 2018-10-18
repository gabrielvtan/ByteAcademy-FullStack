#!/usr/bin/env bash


apt-get -y install firewalld

firewall-cmd --add-port=5002/tcp --permanent

systemctl reload firewalld