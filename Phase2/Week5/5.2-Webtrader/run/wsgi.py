#!/usr/bin/env python3

from src import omnibus


# FIXME Local environment parameters are being passed to the following invocation
omnibus.run(host='0.0.0.0',port=5002,debug=True)

