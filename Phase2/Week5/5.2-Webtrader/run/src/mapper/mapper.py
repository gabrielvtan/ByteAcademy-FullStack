# log in and register SQL
import sqlite3
from pprint import pprint

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

    def cash_balance(self, user_id):
        sql = """SELECT cash_balance FROM users WHERE user_id == '{}';""".format(user_id) 
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result = ((result[0][0]))
        return result



    def check_ticker_status(self, user_id, ticker_symbol):
        sql = """SELECT ticker FROM portfolio WHERE user_id == '{}' and ticker == '{}';""".format(user_id, ticker_symbol)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            return (True)
        else:
            return (False)
    
    def check_log_in(self, user_id, password):
        sql = """SELECT user_id FROM users WHERE user_id == '{}' and password == '{}';""".format(user_id, password)
        self.cursor.execute(sql)
        user_id = self.cursor.fetchall()
        user_id = ((user_id[0][0]))
        return user_id

    def check_volume(self, user_id, ticker_symbol):
        sql = """SELECT volume FROM portfolio WHERE user_id == '{}' and ticker == '{}'; """.format(user_id, ticker_symbol)
        self.cursor.execute(sql)
        current_volume = self.cursor.fetchall()
        current_volume = ((current_volume[0][0]))
        return current_volume


    def create_table(self, table_name):
        self.cursor.execute(
            """CREATE TABLE {table_name} (
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(
                table_name = table_name
            )
        )


    def get_tickers(self):
        sql = """SELECT ticker FROM portfolio;"""
        self.cursor.execute(sql)
        tickers = self.cursor.fetchall()
        ticker_list = []
        for ticker in tickers:
            ticker_list.append(ticker[0])
        return ticker_list


    def get_tickers_users(self, user_id):
        sql = """SELECT ticker FROM portfolio WHERE user_id = '{}';""".format(user_id)
        self.cursor.execute(sql)
        tickers = self.cursor.fetchall()
        ticker_list = []
        for ticker in tickers:
            ticker_list.append(ticker[0])
        return ticker_list

    def get_users(self):
        sql = """SELECT user_id FROM users;"""
        self.cursor.execute(sql)
        users = self.cursor.fetchall()
        user_list = []
        for user in users:
            user_list.append(user[0])
        return user_list
    
    def leaderboard(self):
        sql = """SELECT user_id, SUM(total_value) 
                FROM (
                    SELECT user_id, cash_balance AS total_value
                    FROM users
                    UNION
                    SELECT user_id, SUM(total_value) AS total_value
                    FROM portfolio 
                    GROUP BY user_id
                ) GROUP BY user_id
                ORDER BY total_value DESC
            ;"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def new_buy_portfolio(self, user_id, ticker_symbol, trade_volume, last_price):
        self.cursor.execute(
            """INSERT INTO portfolio (
                user_id,
                ticker,
                volume,
                last_price,
                total_value
                ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
            );""", (user_id,
                    ticker_symbol,
                    trade_volume,
                    last_price,
                    trade_volume*last_price
            )
        )


    def new_transction(self, user_id, date, ticker_symbol, trade_volume, last_price):
        self.cursor.execute(
            """INSERT INTO transactions (
                user_id,
                date, 
                ticker,
                volume,
                last_price
                ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
            );""", (user_id,
                    date,
                    ticker_symbol,
                    trade_volume,
                    last_price
            )
        )


    def new_user(self, user_id, password):  
        self.cursor.execute(
            """INSERT INTO users(
                user_id,
                password,
                cash_balance
                ) VALUES (
                ?,
                ?,
                ?
            );""", (user_id,
                    password,
                    10000.
            )
        )

    def total_portfolio(self, user_id):
        sql ="""SELECT SUM(total_value) 
                FROM (SELECT cash_balance AS total_value 
                    FROM users WHERE user_id = '{}' 
                    UNION 
                    SELECT SUM(total_value) AS total_value 
                    FROM portfolio WHERE user_id = '{}')
            ;""".format(user_id, user_id)
        self.cursor.execute(sql)
        total_portfolio = self.cursor.fetchall()
        return ((total_portfolio[0][0]))


    def update_portfolio_existing(self, user_id, ticker_symbol, trade_volume, last_price):
        sql = """SELECT volume FROM portfolio WHERE ticker == '{}';""".format(ticker_symbol)
        self.cursor.execute(sql)
        total_volume = self.cursor.fetchall()
        total_volume = int(((total_volume[0][0]))) + trade_volume
        sql1 = """UPDATE portfolio SET volume = '{}', 
                    last_price = '{}', 
                    total_value = '{}' 
                    WHERE user_id == '{}' 
                    and ticker == '{}';""".format(total_volume, last_price, total_volume*last_price, user_id, ticker_symbol)
        self.cursor.execute(sql1)
        return self.cursor.fetchall()
    
    def update_user_balance(self, user_id, ticker_symbol, volume, last_price):
        sql1 = """UPDATE portfolio SET last_price = '{}', 
            total_value = '{}' 
            WHERE user_id == '{}' 
            and ticker == '{}';""".format(last_price, volume*last_price, user_id, ticker_symbol)
        self.cursor.execute(sql1)
        return self.cursor.fetchall()        


    def update_balance(self, user_id, cash_balance, total):
        remaining_balance = cash_balance - total
        sql = """UPDATE users SET cash_balance = '{}' WHERE user_id == '{}';""".format(remaining_balance, user_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def update_last_price(self, last_price, ticker):
        sql = """UPDATE portfolio SET last_price = '{}' WHERE ticker = '{}';""".format(last_price, ticker)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


    def view_table(self, table_name):
        sql = """SELECT * FROM '{}' """.format(table_name)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def view_user_positions(self, user_id):
        sql = """SELECT ticker, volume, last_price, total_value FROM portfolio WHERE user_id = '{}'""".format(user_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    


if __name__ == '__main__':
    user_id = 'Gabby'
    password = 123
    with Database('web_trader.db') as db:
        print(db.view_user_positions(user_id))


