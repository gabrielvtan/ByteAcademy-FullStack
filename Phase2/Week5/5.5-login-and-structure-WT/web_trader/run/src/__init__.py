#!/usr/bin/env python3

import os

from flask import Flask

from .controllers.public import controller as public_controller
from .controllers.private import controller as private_controller


omnibus = Flask(__name__)

omnibus.register_blueprint(public_controller)
omnibus.register_blueprint(private_controller)

def keymaker(supercontroller,filename='secret_key.txt'):
    pathname = os.path.join(supercontroller.instance_path,filename)
    try:
        supercontroller.secret_key = open(pathname,'rb').read()
    except IOError:
        path_to_parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(path_to_parent_directory):
            os.system('mkdir -p {pathname}'.format(pathname=path_to_parent_directory))
        os.system('head -c 24 /dev/urandom > {filename}'.format(filename=pathname))
        supercontroller.secret_key = open(pathname,'rb').read()

keymaker(omnibus)
