#!/usr/bin/env python3

import sqlite3

# Use this to change database names
# What is the need to share connections across multiple threads?
# How do you view the labels of the columns? 
connection = sqlite3.connect('class_many_students1.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute( 
    """CREATE TABLE class(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        class_id VARCHAR(32),
        class_name VARCHAR(32),
        teacher_id VARCHAR(32),
        student_id VARCHAR(32)
    );"""
)

cursor.execute( 
    """CREATE TABLE students(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        first VARCHAR(32),
        last VARCHAR(32),
        student_id VARCHAR(32),
        FOREIGN KEY (student_id) REFERENCES class(id)
    );"""
)

db.create_table(students)

cursor.close()
connection.close()