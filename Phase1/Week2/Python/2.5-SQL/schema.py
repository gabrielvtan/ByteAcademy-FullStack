#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('school2.db', check_same_thread = False)
cursor = connection.cursor()

# class_id:
# 1 - Thema, 2 - Psylon, 3 - X-Men


cursor.execute(
    """CREATE TABLE class(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        class_id VARCHAR(32),
        teacher_id VARCHAR(32),
        student_id VARCHAR(32),
        FOREIGN KEY (student_id) REFERENCES student(student_id),
        FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id),
        UNIQUE (student_id, teacher_id)
    );"""
)

# student_id:
# 1 - Gabby, 2 - Matt, 3 - Jason, 4-Kenny
# 1 - Adam, 2 - Cal, 3 - Advi 
# 1 - Jun, 2 - Aileen, 3 - John

cursor.execute(
    """CREATE TABLE student(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id VARCHAR(32),
        first VARCHAR(32),
        last VARCHAR(32),
        city VARCHAR(32)
    );"""
)

# teacher_id:
# 1 - Kenso, 2 - Carter, 3 - Greg

cursor.execute(
    """CREATE TABLE teacher(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_id VARCHAR(32),
        first VARCHAR(32),
        last VARCHAR(32),
        project VARCHAR(32)
    );"""
)

cursor.close()
connection.close()