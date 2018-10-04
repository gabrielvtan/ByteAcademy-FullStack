# log in and register SQL
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

    def check_ticker_status(self, user_id, ticker_symbol):
        sql = """SELECT ticker FROM portfolio WHERE user_id == '{}' and ticker == '{}';""".format(user_id, ticker_symbol)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            return (True)
        else:
            return (False)
    
    def create_table(self, table_name):
        self.cursor.execute(
            """CREATE TABLE {table_name} (
                pk INTEGER PRIMARY KEY AUTOINCREMENT
            );""".format(
                table_name = table_name
            )
        )


    def log_in_information(self, user_id, password):
        sql = """SELECT cash_balance FROM users WHERE user_id == '{}' AND password == '{}';""".format(user_id, password) 
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result = ((result[0][0]))
        return result

    def new_buy_portfolio(self, user_id, ticker_symbol, trade_volume):
        self.cursor.execute(
            """INSERT INTO portfolio (
                user_id,
                ticker,
                volume
                ) VALUES (
                ?,
                ?,
                ?
            );""", (user_id,
                    ticker_symbol,
                    trade_volume
            )
        )

    def new_buy_transctions(self, user_id, date, ticker_symbol, trade_volume, cost_basis):
        self.cursor.execute(
            """INSERT INTO transactions (
                user_id,
                date, 
                ticker,
                volume,
                cost_basis
                ) VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
            );""", ('{}'.format(user_id),
                    '{}'.format(date),
                    '{}'.format(ticker_symbol),
                    '{}'.format(trade_volume),
                    '{}'.format(cost_basis)
            )
        )
    
    ## YOU NEED TO FIX THIS 
    def update_portfolio_existing(self, user_id, ticker_symbol, trade_volume):
        sql = """SELECT volume FROM portfolio WHERE ticker == '{}';""".format(ticker_symbol)
        self.cursor.execute(sql)
        total_volume = self.cursor.fetchall()
        total_volume = int(((total_volume[0][0]))) + trade_volume
        sql1 = """UPDATE portfolio SET volume = '{}' where user_id == '{}' and ticker == '{}';""".format(total_volume, user_id, ticker_symbol)
        self.cursor.execute(sql1)
        return self.cursor.fetchall()
        
    ## YOU NEED TO FIX THIS 
    def update_balance(self, user_id, cash_balance, total):
        #update table_name SET column_name = "value" where user_id = ""
        remaining_balance = cash_balance - total
        sql = """UPDATE users SET cash_balance = '{}' where user_id == '{}'""".format(remaining_balance, user_id)
        self.cursor.execute(sql)
        return self.cursor.fetchall()




if __name__ == '__main__':
    user_id = 'Gabby'
    password = 1234
    ticker_symbol = 'GOOG'
    trade_volume = 100
    with Database('terminal_trader.db') as db:
        result = db.update_portfolio_existing(user_id, ticker_symbol, trade_volume)
        print(result)

