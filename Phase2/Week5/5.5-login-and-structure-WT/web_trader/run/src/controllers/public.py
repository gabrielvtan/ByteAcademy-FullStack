#!/usr/bin/env python3

from flask import Blueprint,render_template,request


controller = Blueprint('public',__name__)


@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        # FIXME - Finish writing the following condition
        pass
    else:
        # FIXME - Finish writing the following condition
        pass


@controller.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
