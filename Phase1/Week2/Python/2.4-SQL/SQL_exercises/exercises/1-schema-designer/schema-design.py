#!/usr/bin/env python3

import sqlite3

# Use this to change database names
# What is the need to share connections across multiple threads?
# How do you view the labels of the columns? 
connection = sqlite3.connect('snacks.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute( 
    """CREATE TABLE snacks(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        brand VARCHAR(32),
        type VARCHAR(32),
        price VARCHAR(32),
        quantity VARCHAR(32)
    ); """
)

cursor.close()
connection.close()