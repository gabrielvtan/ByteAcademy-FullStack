#!/usr/bin/env python3

from flask import Blueprint,render_template,request, session


controller = Blueprint('public',__name__)


@controller.route('/',methods=['GET','POST'])
def frontpage():
    if request.method == 'GET':
        return render_template('index.html')



@controller.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
       username = request.form["username"]
       password = request.form["password"]
       if username and password:
        
    else:
        # FIXME - Finish writing the following condition
        pass
