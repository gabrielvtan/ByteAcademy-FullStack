#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('monty_hall.db', check_same_thread = False)
cursor = connection.cursor()

#query = "selece * from ? where name = ? "
#cursor.execute(query, varaible) 

cursor.execute(
    """CREATE TABLE monty_hall(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        winning_door VARCHAR(32),
        first_choice VARCHAR(32),
        outcome BOOL
    );"""
)


cursor.close()
connection.close()