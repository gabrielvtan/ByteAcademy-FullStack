## Create a DB from CSV data

In this challenge, you will be asked to import CSV data into a sqlite database.

In the CSV file, you will find a person with a name, email, country of residence, and three phone numbers.

Create a users table and a phone numbers table. The relation is that a user has many phone numbers.

When you have done that, use Python's sqlite3 library to create the tables.

#### SQLite 3

Take a look here at Python's sqlite driver [documentation](https://docs.python.org/3.4/library/sqlite3.html)

You need to establish a database and a cursor object.
```py
import sqlite3
conn = sqlite3.connect('mydb.db')
c = conn.cursor()
```
To create a table:
```py
c.execute("CREATE TABLE 'users' (
'id' INTEGER,
'name' VARCHAR,
'account' VARCHAR,
'balance' REAL,
PRIMARY KEY ('id')
)")
```
To insert a row of data:
```py
c.execute("INSERT INTO users(name, account, balance) VALUES(?,?,?)", (name, account, balance))
```
**Note: ** You must specify the columns names otherwise sqlite3 will default to all columns. 

Sandbox! dir() and help() the cursor for all the methods possible.

What does executemany do?

What are your options for fetch?

#### CSV

Take a look at the CSV library for Python's [documentation](https://docs.python.org/3.4/library/csv.html)

Sandbox some more with CSV.

Import the file using Python's csv library and figure out how to write this data into the appropriate table and column in the db.
