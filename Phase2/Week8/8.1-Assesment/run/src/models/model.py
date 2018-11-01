#!/usr/bin/env python3

database = 'run/src/datastores/master.db'

from flask import Flask, render_template, request, session
from src.mappers.sqlite import Database
from datetime import datetime

def check_log_in(user_id, password):
    with Database(database) as db:
        return db.check_log_in(user_id, password)

def check_friend_id(friend_id):
    with Database(database) as db:
        return db.check_friend_id(friend_id)

def date_now():
    return datetime.now()

def grab_tweets(friend_id):
    with Database(database) as db:
        return db.grab_tweets(friend_id)

def new_user(user_id, password):
    with Database(database) as db:
        return db.new_user(user_id,password)

def new_tweet(user_id, tweet):
    date = date_now()
    with Database(database) as db:
        db.new_tweet(user_id, tweet, date)

def add_new_friend(user_id, friend_id):
    with Database(database) as db:
        db.add_new_friend(user_id,friend_id)








