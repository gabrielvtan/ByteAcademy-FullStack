#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('user_admin.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE user(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        user_name VARCHAR(32),
        password VARCHAR(32),
        email VARCHAR(32),
        phone_numbers_id VARCHAR(32),
        FOREIGN KEY (phone_numbers_id) REFERENCES phonebook(phone_numbers_id),
        UNIQUE (user_name, phone_numbers_id)
    );"""
)

cursor.execute(
    """CREATE TABLE admin(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32),
        user_name VARCHAR(32),
        password VARCHAR(32),
        email VARCHAR(32),
        phone_numbers_id VARCHAR(32),
        FOREIGN KEY (phone_numbers_id) REFERENCES phonebook(phone_numbers_id),
        UNIQUE (user_name, phone_numbers_id)
    );"""
)

cursor.execute(
    """CREATE TABLE phonebook(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_numbers_id VARCHAR(32),
        mobile VARCHAR(32),
        home VARCHAR(32),
        office VARCHAR(32)
    );"""
)

cursor.close()
connection.close()