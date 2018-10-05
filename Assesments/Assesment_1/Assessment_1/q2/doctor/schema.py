#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('medical.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE patient(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name VARCHAR(32),
        doctor_name VARCHAR(32),
        doctor_type VARCHAR(32)
    );"""
)

cursor.execute(
    """CREATE TABLE doctor(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor_name VARCHAR(32),
        patient_name VARCHAR(32)
    );"""
)

cursor.close()
connection.close()