#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('test.db', check_same_thread = False)
cursor = connection.cursor()

# pk = primary copy
cursor.execute(
    """INSERT INTO users(
        username, 
        password
        ) VALUES(
        ?,
        ?
    ); """, (
        'kensotrabing',
        'swordfish'
    )
)

# always need to close cursor before closing the connect
connection.commit() # this is kind-of like saving your changes
cursor.close()
connection.close()
