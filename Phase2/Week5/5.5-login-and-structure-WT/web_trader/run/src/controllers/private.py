#!/usr/bin/env python3

from flask import Blueprint,render_template,request


controller = Blueprint('private',__name__,url_prefix='/private')


@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # FIXME - Finish writing the following condition
        pass
    else:
        # FIXME - Finish writing the following condition
        pass
