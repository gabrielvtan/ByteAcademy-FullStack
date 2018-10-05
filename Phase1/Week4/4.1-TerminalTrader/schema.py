#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('terminal_trader.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32),
        password VARCHAR(32),
        cash_balance DECIMAL,
        UNIQUE (user_id)
    );"""
)

cursor.execute(
    """CREATE TABLE transactions(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32),
        date DATETIME, 
        ticker VARCHAR(32),
        volume DECIMAL,
        last_price DECIMAL
    );"""
)

cursor.execute(
    """CREATE TABLE portfolio(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id VARCHAR(32),
        ticker VARCHAR(32),
        volume DECIMAL,
        last_price DECIMAL,
        total_value DECIMAL
    );"""
)

cursor.close()
connection.close()