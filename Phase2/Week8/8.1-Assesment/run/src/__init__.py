#!/usr/bin/env python3

from flask import Flask, render_template

omnibus = Flask(__name__)

@omnibus.route('/')
def f():
    return render_template('unauthorized/index.html')
