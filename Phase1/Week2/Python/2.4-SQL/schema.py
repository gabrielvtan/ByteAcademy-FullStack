#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('test.db', check_same_thread = False)
cursor = connection.cursor()

# pk = primary copy
cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32)
    ); """
)

# always need to close cursor before closing the connect
cursor.close()
connection.close()
