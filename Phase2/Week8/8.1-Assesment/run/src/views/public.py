#!/usr/bin/env python3

from flask import Blueprint,render_template,request, session, Flask, redirect

from src.models import model
from src.mappers.sqlite import Database


controller = Blueprint('public',__name__)

#controller = Flask(__name__)
controller.secret_key = "12344666689"

@controller.route('/admin', methods=['GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')


@controller.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('unauthorized/login.html')
    elif request.method == 'POST':
        session['user_id'] = request.form['user_id']
        password = request.form['password']
        # if session['user_id'] == 'Admin' and password == 'Admin':
        #     return render_template('admin.html')
        # else:
        try:
            user_id = model.check_log_in(session['user_id'], password)
            #message = "Welcome to your Gabber homepage {}. What would you like to do?".format(user_id)
            return redirect ('/newsfeed')
        except TypeError:
            message = "Invalid credentials"
            return render_template('unauthorized/login.html', message=message)


@controller.route('/signup', methods =['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('unauthorized/signup.html')
    elif request.method == 'POST':
        user_id = request.form['user_id']
        password = request.form['password']
        try:
            model.new_user(user_id, password)
            message = "You have successfully created a new account"
            return render_template('unauthorized/login.html', message=message)
        except TypeError:
            message = "Invalid credentials"
            return render_template('unauthorized/signup.html', message=message)


@controller.route('/newsfeed', methods = ['GET', 'POST'])
def newsfeed():
    if request.method == 'GET':
        return render_template('authorized/newsfeed.html')
    elif request.method == 'POST':
        user_id = session['user_id']
        tweet = request.form['tweet']
        model.new_tweet(user_id,tweet)
        message = "Success"
        return render_template('authorized/newsfeed.html', message=message)


@controller.route('/account', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        session['friend_id'] = request.form['friend_id']
        result = model.check_friend_id(session['friend_id'])
        friend_id = session['friend_id']
        if result:
            message = friend_id
            try:
                all_tweets = model.grab_tweets(friend_id)
                dates = []
                tweets = []
                tweet_list = []
                for row in all_tweets:
                    dates.append(row[0])
                    tweets.append(row[1])
                for num in range (0, len(dates)):
                    tweet_list.append((dates[num], tweets[num]))
                return render_template('authorized/account.html', message=message, tweet_list=tweet_list, friend_id=friend_id)
            except TypeError:
                message = "Invalid user selection"
                return render_template('authorized/newsfeed.html', message=message)


@controller.route('/follow', methods =["GET", "POST"])
def add_friend():
    if request.method == 'GET':
        friend_id = session['friend_id']
        return render_template ('authorized/account.html', friend_id=friend_id)
    elif request.method == 'POST':
        user_id = session['user_id']
        friend = request.form['add_friend']
        model.add_new_friend(user_id, friend)
        all_tweets = model.grab_tweets(friend)
        dates = []
        tweets = []
        tweet_list = []
        for row in all_tweets:
            dates.append(row[0])
            tweets.append(row[1])
        for num in range (0, len(dates)):
            tweet_list.append((dates[num], tweets[num]))
        message = friend
        message2 = "You have started following {}".format(friend)
        return render_template ('authorized/account.html', tweet_list=tweet_list, message=message, message2=message2)        
