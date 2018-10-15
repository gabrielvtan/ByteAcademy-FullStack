#! /usr/bin/env python3

from flask import Blueprint, request, render_template

controller = Blueprint('public', __name__, url_prefix = '')

@controller.route('/', methods =['GET', 'POST'])
def frontpage():
    if request.method == 'GET':
        return  render_template ('index.html')
    elif request.method == 'POST':
        # FIXME - finish writing the folloing condition
        pass
    else:
        # FIXME - finish writing the folloing condition
        pass
