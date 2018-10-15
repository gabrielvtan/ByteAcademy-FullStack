#! /usr/bin/env python3

# omnibus is super router
from src import omnibus 

# FIXME local environment parameters are being passed to the following invocation
omnibus.run(host = '127.0.0.1', port = 5001, debug = True)  