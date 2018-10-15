#!/usr/bin/env python3

from src import omnibus


# FIXME Local environment parameters are being passed to the following invocation
omnibus.run(host='127.0.0.1',port=5000,debug=True)

