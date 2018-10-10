#!/usr/bin/env python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def frontpage():
    if request.method == 'GET':
        message = 'Welcome to Web. Trader'
        return render_template('index.html', message=message)
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username and password:
            if username == 'kenso' and password == 'opensesame':
                message = 'You have successfully logged into your applicaton'
                return render_template('index.html', message=message)
            else:
                message = 'Please enter valid credentials'
                return render_template('index.html', message=message)


@app.route('/grandpa',methods=['GET','POST'])
def grandpa():
    if request.method == 'GET':
        message = 'Hello, Grandson'
        return render_template('grandpa.html',message=message)
    elif request.method == 'POST':
        forename = request.form['forename']
        message = request.form['message']
        if forename and message:
            if forename.isupper() and message.isupper():
                spoken_word = "{}, you said {}, back in my day we would never say that...".format(forename,message )
                return render_template('grandpa.html', message=spoken_word)
            elif forename.islower() or message.islower():
                spoken_word ="Speak with authority you little prick... I can't hear you."
                return render_template('grandpa.html', message=spoken_word)


if __name__ == '__main__':
    app.run("127.0.0.1", port=5001, debug=True)