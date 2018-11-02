#!/usr/bin/env python3

from flask import Blueprint,render_template,request, session, Flask, redirect

from src.models import model
from src.mappers.sqlite import Database

controller = Blueprint('public',__name__)

controller.secret_key = "12344666689"

@controller.route('/follow', methods =["GET", "POST"])
def add_friend():
    if request.method == 'GET':
        friend_id = session['friend_id']
        return render_template ('authorized/account.html', friend_id=friend_id)
    elif request.method == 'POST':
        try:
            user_id = session['user_id']
            friend = request.form['add_friend']
            model.add_new_friend(user_id, friend)
            tweet_list = model.grab_tweets(friend)
            message = friend
            message2 = "You have started following {}".format(friend)
            return render_template ('authorized/account.html', tweet_list=tweet_list, message=message, message2=message2)        
        except:
            user_id = session['user_id']
            retweet = request.form['retweet']
            model.new_tweet(user_id, retweet)
            tweet_list = model.grab_friend_tweets(user_id)
            return render_template('authorized/newsfeed.html', tweet_list=tweet_list)


@controller.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'GET':
        user_id = session['user_id']
        message = user_id
        tweet_list = model.landingpage()
        return render_template('authorized/admin.html', tweet_list=tweet_list, message=message)


@controller.route('/admin/account', methods = ['GET', 'POST'])
def admin_search():
    if request.method == 'GET':
        return render_template('authorized/adminAccount.html')
    elif request.method == 'POST':
        session['friend_id'] = request.form['friend_id']
        result = model.check_friend_id(session['friend_id'])
        if result:
            friend_id = session['friend_id']
            message = friend_id
            tweet_list = model.account_tweets(friend_id)
            return render_template('authorized/adminAccount.html', message=message, tweet_list=tweet_list, friend_id=friend_id)
        else:
            message3 = "Invalid user selection"
            return render_template('authorized/admin404.html', message3=message3)


@controller.route('/delete', methods =["GET", "POST"])
def delete_account():
    if request.method == 'GET':
        friend_id = session['friend_id']
        return render_template ('authorized/adminAccount.html', friend_id=friend_id)
    elif request.method == 'POST':
        user_id = session['user_id']
        friend_id = request.form['delete_account']
        message = "Deleted the account of {}".format(friend_id)
        model.delete_account(friend_id)
        tweet_list = model.landingpage()
        return render_template('authorized/admin.html', tweet_list=tweet_list, message=message)


@controller.route('/', methods =['GET', 'POST'])
def landingpage():
    tweet_list = model.landingpage()
    if request.method == 'GET':
        return render_template('unauthorized/index.html', tweet_list=tweet_list)


@controller.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('unauthorized/login.html')
    elif request.method == 'POST':
        session['user_id'] = request.form['user_id']
        password = request.form['password']
        if session['user_id'] == 'Admin' and password == 'Admin':
             return redirect ('/admin')
        else:
            try:
                user_id = model.check_log_in(session['user_id'], password)
                return redirect ('/newsfeed')
            except:
                message = "Invalid credentials"
                return render_template('unauthorized/login.html', message=message)


@controller.route('/newsfeed', methods = ['GET', 'POST'])
def newsfeed():
    if request.method == 'GET':
        user_id = session['user_id']
        tweet_list = model.grab_friend_tweets(user_id)
        return render_template('authorized/newsfeed.html', tweet_list=tweet_list)
    elif request.method == 'POST':
        try:
            user_id = session['user_id']
            tweet = request.form['tweet']
            model.new_tweet(user_id,tweet)
        except:
            user_id = session['user_id']
            retweet = request.form['retweet']
            model.new_tweet(user_id, retweet)
        tweet_list = model.grab_friend_tweets(user_id)
        return render_template('authorized/newsfeed.html', tweet_list=tweet_list)


@controller.route('/account', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        try:
            session['friend_id'] = request.form['friend_id']
            result = model.check_friend_id(session['friend_id'])
            friend_id = session['friend_id']
            if result:
                message = friend_id
                tweet_list = model.account_tweets(friend_id)
                return render_template('authorized/account.html', message=message, tweet_list=tweet_list, friend_id=friend_id)
            else:
                user_id = session['user_id']
                retweet = request.form['retweet']
                model.new_tweet(user_id, retweet)
                tweet_list = model.grab_friend_tweets(user_id)
                return render_template('authorized/newsfeed.html', tweet_list=tweet_list)     
        except:
            message3 = "Invalid user selection"
            return render_template('authorized/404.html', message3=message3)


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
        except:
            message = "User ID already exists"
            return render_template('unauthorized/signup.html', message=message)

