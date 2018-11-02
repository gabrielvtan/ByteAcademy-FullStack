#!/usr/bin/env python3

database = 'run/src/datastores/master.db'

from flask import Flask, render_template, request, session
from src.mappers.sqlite import Database
from datetime import datetime

def add_new_friend(user_id, friend_id):
    with Database(database) as db:
        db.add_new_friend(user_id,friend_id)

def account_tweets(friend_id):
    all_tweets = grab_tweets(friend_id)
    dates = []
    tweets = []
    tweet_list = []
    for row in all_tweets:
        dates.append(row[0])
        tweets.append(row[1])
    for num in range (0, len(dates)):
        tweet_list.append((dates[num], tweets[num]))
    return tweet_list


def check_log_in(user_id, password):
    with Database(database) as db:
        return db.check_log_in(user_id, password)


def check_friend_id(friend_id):
    with Database(database) as db:
        return db.check_friend_id(friend_id)


def date_now():
    return datetime.now()


def delete_account(friend_id):
    with Database(database) as db:
        db.delete_user(friend_id)
        db.delete_tweets(friend_id)
        db.delete_friends(friend_id)


def grab_tweets(friend_id):
    with Database(database) as db:
        return db.grab_tweets(friend_id)


def grab_friend_tweets(user_id):
    friend_list = newsfeed_friendlist(user_id)
    tweet_list_raw = []
    for friend in friend_list:
        tweet_list_raw.append(newsfeed(friend))
    tweet_list_unsorted = []
    for user in tweet_list_raw:
        for tweet in user:
            tweet_list_unsorted.append(tweet)
    tweet_list_sorted = sorted(tweet_list_unsorted, key=lambda x:x[0], reverse=True)
    dates = []
    users = []
    tweets = []
    tweet_list =[]
    for row in tweet_list_sorted:
        dates.append(row[0])
        users.append(row[1])
        tweets.append(row[2])
    for num in range(0, len(dates)):
        tweet_list.append((dates[num],users[num],tweets[num]))
    return tweet_list


def landingpage():
    with Database(database) as db:
        all_tweets = db.landingpage()
        dates = []
        users = []
        tweets = []
        tweet_list =[]
        for row in all_tweets:
            dates.append(row[0])
            users.append(row[1])
            tweets.append(row[2])
        for num in range(0, len(dates)):
            tweet_list.append((dates[num],users[num],tweets[num]))
        return tweet_list

def new_user(user_id, password):
    with Database(database) as db:
        return db.new_user(user_id,password)


def new_tweet(user_id, tweet):
    date = date_now()
    with Database(database) as db:
        db.new_tweet(user_id, tweet, date)
        


def newsfeed(user_id):
    with Database(database) as db:
        return db.newsfeed(user_id)


def newsfeed_friendlist(user_id):
    with Database(database) as db:
        friend_list = db.grab_friends(user_id)
        friend_list.append(user_id)
        return friend_list



if __name__ == '__main__':
    print(newsfeed('Gabby'))







