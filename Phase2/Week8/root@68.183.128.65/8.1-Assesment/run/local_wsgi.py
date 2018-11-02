#!/usr/bin/env python3

from src import omnibus

if __name__ == '__main__':
    print('WARNING: PARAMETERS ARE SET FOR A LOCAL ENVIRONMENT')
    omnibus.run(host='127.0.0.1', port = 5002, debug=True)