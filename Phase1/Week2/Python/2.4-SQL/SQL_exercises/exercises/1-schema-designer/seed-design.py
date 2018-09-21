#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('class_many_students1.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO class(
        class_id,
        class_name,
        teacher_id,
        student_id
        ) VALUES(
        ?,
        ?,
        ?,
        ?
    ); """, (
        'BYTE',
        'THEMA',
        'GREG',
        'MATT'
    )
)

cursor.execute(
    """INSERT INTO class(
        class_id,
        class_name,
        teacher_id,
        student_id
        ) VALUES(
        ?,
        ?,
        ?,
        ?
    ); """, (
        'BYTE',
        'THEMA',
        'GREG',
        'GABBY'
    )
)

cursor.execute(
    """INSERT INTO students(
        first,
        last,
        student_id
        ) VALUES(
        ?,
        ?,
        ?
    ); """, (
        'Matt',
        'Neely',
        'MATT'
    )
)

cursor.execute(
    """INSERT INTO students(
        first,
        last,
        student_id
        ) VALUES(
        ?,
        ?,
        ?
    ); """, (
        'Gabby',
        'Tan',
        'GABBY'
    )
)

connection.commit()
cursor.close()
connection.close()