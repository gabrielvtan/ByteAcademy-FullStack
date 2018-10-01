# Quiz: take Yahoo finance market data (this .csv) and put *all of it* into a SQLite database. 
# Send me (via direct message) a zip of your python file(s) and database by 11:00

import csv
import sqlite3
from model import Database

file = 'TSLA.csv'
tsla_database = 'TSLA.db'

 
def open_csv(file):
    with Database(tsla_database) as db:
        with open(file, 'r') as open_file:
            rows = csv.reader(open_file)
            next(rows, None)
            for row in rows:
                open_ = row[0]
                high = row[1]
                low = row[2]
                close = row[3]
                adjusted = row[4]
                volume = row[5]
                db.add_entry(open_, high, low, close, adjusted, volume)
            





open_csv(file)
