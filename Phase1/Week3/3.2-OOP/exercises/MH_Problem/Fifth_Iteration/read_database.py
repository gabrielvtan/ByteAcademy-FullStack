import sqlite3

class Database:
    """
    Class for querying the results of the Monty Hall Problem
    """
    
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

    def monty_hall_results_true(self, table_name):
       sql =  """SELECT COUNT(outcome) FROM {} WHERE outcome == 'True';""".format(table_name)
       self.cursor.execute(sql)
       result = self.cursor.fetchall()
       return result

    def monty_hall_results_false(self, table_name):
       sql =  """SELECT COUNT(outcome) FROM {} WHERE outcome == 'False';""".format(table_name)
       self.cursor.execute(sql)
       result = self.cursor.fetchall()
       return result