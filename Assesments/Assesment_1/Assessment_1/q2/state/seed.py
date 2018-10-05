import sqlite3

connection = sqlite3.connect('state.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO state(
        state_name,
        city_name,
        park_name
        ) VALUES (
        ?,
        ?,
        ?
    );""", (
        'North Carolina',
        'Black Mountain',
        'Witch Park'
    )
)

connection.commit()
cursor.close()
connection.close()
