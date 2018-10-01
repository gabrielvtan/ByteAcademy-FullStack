import sqlite3

connection = sqlite3.connect('TSLA.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE tsla(
        pk INTEGER PRIMARY KEY AUTOINCREMENT, 
        Open DECIMAL,
        High DECIMAL,
        Low DECIMAL,
        Close DECIMAL,
        Adjusted DECIMAL,
        Volume DECIMAL
    );"""
)

cursor.close()
connection.close()