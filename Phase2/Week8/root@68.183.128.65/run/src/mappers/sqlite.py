#!/usr/bin/env python3

import sqlite3

class Database:
    def __init__(self, pathname):
        #Pathname is the path to the file and filename
        self.connection = sqlite3.connect(pathname, check_same_thread = False)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if self.connection:
            if self.cursor:
                self.cursor.close()
            self.connection.commit()
            self.connection.close()
    
    
    def add_column(self, table_name, column_name, column_type):
        self.cursor.execute(
            """ ALTER TABLE {table_name}
                ADD COLUMN {column_name} {column_type}
            ;""".format(
                table_name = table_name,
                column_name = column_name,
                column_type = column_type
            )
        )
    
    
    def add_new_friend(self, user_id, friend_id):
        self.cursor.execute(
            """INSERT INTO friends(
                user_id,
                friend_id
                ) VALUES (
                ?,
                ?
            );""", (user_id,
                    friend_id
            )
        )            
    
    def check_friend_id(self, friend_id):
        try:
            sql = """SELECT * FROM users WHERE user_id == '{}';""".format(friend_id)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                return True
        except TypeError:
            return False


    def check_log_in(self, user_id, password):
        sql = """SELECT user_id FROM users WHERE user_id == '{}' and password == '{}';""".format(user_id, password)
        self.cursor.execute(sql)
        user_id = self.cursor.fetchall()
        user_id = ((user_id[0][0]))
        return user_id


    def create_table(self, tablename):
        self.cursor.execute(
            """CREATE TABLE {tablename} (
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(tablename=tablename)
        )

    


    def grab_tweets(self, friend_id):
        sql = """SELECT date, tweet FROM tweets WHERE user_id == '{}' ORDER BY date DESC;""".format(friend_id)
        self.cursor.execute(sql)
        tweets = self.cursor.fetchall()
        return tweets

    
    def grab_friends(self, user_id):
        sql = """SELECT friend_id FROM friends WHERE user_id == '{}';""".format(user_id)
        self.cursor.execute(sql)
        friends = self.cursor.fetchall()
        friend_list = []
        for friend in friends:
            friend_list.append(friend[0])
        return friend_list


    def landingpage(self):
        self.cursor.execute("SELECT date, user_id, tweet FROM tweets ORDER BY date DESC;") 
        return self.cursor.fetchall() 


    def new_tweet(self, user_id, tweet, date):
        self.cursor.execute(
            """INSERT INTO tweets(
                user_id,
                date,
                tweet
                ) VALUES (
                ?,
                ?,
                ?
            );""", (user_id,
                    date,
                    tweet
            )
        )
    

    def new_user(self, user_id, password):  
        self.cursor.execute(
            """INSERT INTO users(
                user_id,
                password
                ) VALUES (
                ?,
                ?
            );""", (user_id,
                    password
            )
        )


    def newsfeed(self, user_id):
        sql = """SELECT date, user_id, tweet FROM tweets WHERE user_id == '{}' ORDER BY date DESC;""".format(user_id)
        self.cursor.execute(sql)
        tweets = self.cursor.fetchall()
        return tweets


    def delete_user(self, friend_id):
        sql = """DELETE FROM users WHERE user_id == '{}'""".format(friend_id)
        self.cursor.execute(sql)


    def delete_tweets(self, friend_id):    
        sql = """DELETE FROM tweets WHERE user_id == '{}'""".format(friend_id)
        self.cursor.execute(sql)


    def delete_friends(self,friend_id):
        sql = """DELETE FROM friends WHERE user_id == '{}'""".format(friend_id)
        self.cursor.execute(sql)

if __name__ == '__main__':
    with Database('run/src/datastores/master.db') as db:
        print(db.grab_friends('Gabby'))