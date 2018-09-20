#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('snacks.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO snacks(
        brand,
        type,
        price,
        quantity
        ) VALUES(
        ?,
        ?,
        ?,
        ?
    ); """, (
        'Hostess',
        'Snacky Cakes',
        10,
        100
    )
)

connection.commit()
cursor.close()
connection.close()