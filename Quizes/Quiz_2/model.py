import sqlite3

class Database:
    def __init__(self, database_name):
         self.connection = sqlite3.connect(database_name, check_same_thread = False)
         self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        else:
            print('Unfinished control flow in database')
            pass

    def add_entry(self, open_, high, low, close, adjusted, volume):
        self.cursor.execute(
            """INSERT INTO tsla(
                Open,
                High,
                Low,
                Close,
                Adjusted,
                Volume
                ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
                );""", (
                    '{}'.format(open_),
                    '{}'.format(high),
                    '{}'.format(low),
                    '{}'.format(close),
                    '{}'.format(adjusted),
                    '{}'.format(volume)
                )
            )