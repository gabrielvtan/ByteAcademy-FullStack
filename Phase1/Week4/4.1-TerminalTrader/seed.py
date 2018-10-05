#!/usr/bin/env python3

import model

import sqlite3
from datetime import date, datetime

connection = sqlite3.connect('terminal_trader.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        user_id,
        password,
        cash_balance
        ) VALUES (
        ?,
        ?,
        ?
    );""", (
        'Gabby',
        123,
        100000
    )
)

now = model.time('TSLA')

cursor.execute(
    """INSERT INTO transactions(
        user_id,
        date, 
        ticker,
        volume,
        last_price
        ) VALUES (
        ?,
        ?,
        ?,
        ?,
        ?
    );""", ('Gabby',
            now,
            'TSLA',
            100,
            100
    )
)

cursor.execute(
    """INSERT INTO portfolio(
        user_id,
        ticker,
        volume,
        last_price,
        total_value 
        ) VALUES (
        ?,
        ?,
        ?,
        ?,
        ?
    );""", ('Gabby',
            'TSLA',
            100,
            280,
            28000
    )
)

connection.commit()
cursor.close()
connection.close()

