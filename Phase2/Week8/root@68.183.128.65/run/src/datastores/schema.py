#!/usr/bin/env python3

import sqlite3

database = 'run/src/datastores/master.db'

connection = sqlite3.connect(database, check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32),
        password VARCHAR(32),
        UNIQUE (user_id)
    );"""
)

cursor.execute(
    """CREATE TABLE tweets(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32),
        date DATETIME, 
        tweet VARCHAR(32)
    );"""
)

cursor.execute(
    """CREATE TABLE friends(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32), 
        friend_id VARCHAR(32)
    );"""
)

cursor.close()
connection.close()