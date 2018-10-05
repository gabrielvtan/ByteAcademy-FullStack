#!/usr/bin/env python3

from mapper import Database
from wrapper import Markit
from pprint import pprint
import view

import requests
import json
from datetime import datetime

def buy(user_id, cash_balance):
    (ticker_symbol, trade_volume) = view.buy_menu()
    last_price = quote(ticker_symbol)
    date = time(ticker_symbol)
    fee = 6.95
    total = trade_volume * last_price + fee
    if total > cash_balance:
        view.error_message()
        buy(user_id, cash_balance)
    else:
        with Database ('terminal_trader.db') as db:
            result = db.check_ticker_status(user_id, ticker_symbol)
            db.new_transction(user_id, date, ticker_symbol, trade_volume, last_price)
            db.update_balance(user_id, cash_balance, total)
            if result:
                # update the current portfolio holding for total volume of a given stock
                db.update_portfolio_existing(user_id, ticker_symbol, trade_volume, last_price)
            else:
                # create a new entry in the portfolio
                db.new_buy_portfolio(user_id, ticker_symbol, trade_volume, last_price)



def check_balance(user_id, password):
    with Database('terminal_trader.db') as db:
        balance = round(db.log_in_information(user_id,password), 2)
        return balance

        

def sell(user_id, cash_balance):
    # last_price is actually sale price
    (ticker_symbol, trade_volume) = view.sell_menu()
    last_price = quote(ticker_symbol)
    date = time(ticker_symbol)
    with Database('terminal_trader.db') as db:
        result = db.check_ticker_status(user_id, ticker_symbol)
        current_volume = int(db.check_volume(user_id, ticker_symbol))
        if trade_volume > current_volume:
            view.error_message()
            sell(user_id, cash_balance)
        else:
            trade_volume = -trade_volume
            fee = 6.95
            total = last_price * trade_volume - fee
            # record the transaction in transactoins table
            db.new_transction(user_id, date, ticker_symbol, trade_volume, last_price)
            # decrease volume in portfolio table
            db.update_portfolio_existing(user_id, ticker_symbol, trade_volume, last_price)
            # increase the cash balance 
            db.update_balance(user_id, cash_balance, total)


def leaderboard():
    with Database('terminal_trader.db') as db:
        ticker_list = db.get_tickers()
        for ticker in ticker_list:
            last_price = quote(ticker)
            # NEED TO incorporate updated volume
            # YOU ALREADY WROTE THIS FUNCTION 
            db.update_last_price(last_price, ticker)
        pprint(db.leaderboard())



        


    
def lookup(company_name):
    #endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
    #response = json.loads(requests.get(endpoint).text)
    #return response
    with Markit() as api:
        ticker = api.lookup(company_name)
        print ('The compnay ticker is:',ticker)

def time(ticker_symbol):
    with Markit() as api:
        return api.time_now(ticker_symbol)

def quote(ticker_symbol):
    with Markit() as api:
        return api.quote(ticker_symbol)
        

def view_table(table_name):
    with Database ('terminal_trader.db') as db:
       pprint(db.view_table(table_name))

if __name__ == '__main__':
    print(leaderboard())