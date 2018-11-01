#!/usr/bin/env python3

import sqlite3
from datetime import date, datetime

database = 'run/src/datastores/master.db'

connection = sqlite3.connect(database, check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO friends(
        user_id,
        friend_id
        ) VALUES (
        ?,
        ?
    );""", (
        'Gabby',
        'Matt'
    )
)

connection.commit()
cursor.close()
connection.close()