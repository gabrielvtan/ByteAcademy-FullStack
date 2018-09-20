import sqlite3

class Database:
    # Constructor
    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self 
    
    def __exit__(self, type, value, traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else:
            print('Unfinished control flow in `data_access_object.py`')
            pass

    def create_table(self, table_name):
        self.cursor.execute(
            """CREATE TABLE {table_name} (
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(table_name = table_name)
        )
        return self

    def add_column(self, table_name, column_name):
        self.cursor.execute(
            """ALTER TABLE {table_name}
                ADD COLUMN {column_name}
            ;""".format(
                table_name=table_name, 
                column_name=column_name
            )
        )