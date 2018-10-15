#! /usr/bin/env python3

from flask import Blueprint, request, render_template

controller = Blueprint('private', __name__, url_prefix = '/private')

@controller.route('/', methods =['GET', 'POST'])
def frontpage():
    if request.method == 'GET':
        return  render_template ('login.html')
    elif request.method == 'POST':
        # FIXME - finish writing the folloing condition
        pass
    else:
        # FIXME - finish writing the folloing condition
        pass
