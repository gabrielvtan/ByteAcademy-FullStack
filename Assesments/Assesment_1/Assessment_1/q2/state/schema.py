#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('state.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE state(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        state_name VARCHAR(32),
        city_name VARCHAR(32),
        park_name VARCHAR(32)
    );"""
)

cursor.close()
connection.close()