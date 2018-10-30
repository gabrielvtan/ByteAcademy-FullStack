#!/usr/bin/env bash

wget https://www.multichain.com/download/multichain-1.0.6.tar.gz -O /tmp/multichain.tar.gz

tar -xvzf multichain-1.0.6.tar.gz -C /opt

cd /opt/multichain-1.0.6/

mv multichain-cli multichaind multichain-util /usr/local/bin
