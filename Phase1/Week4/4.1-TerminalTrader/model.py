#!/usr/bin/env python3

from mapper import Database
from wrapper import Markit
import view

import requests
import json
from datetime import datetime

def buy(user_id, cash_balance):
    (ticker_symbol, trade_volume) = view.buy_menu()
    cost_basis = quote(ticker_symbol)
    date = time(ticker_symbol)
    total = trade_volume * cost_basis
    if total > cash_balance:
        view.error_message()
        buy(user_id, cash_balance)
    else:
        with Database ('terminal_trader.db') as db:
            result = db.check_ticker_status(user_id, ticker_symbol)
            print(result)
            db.new_buy_transctions(user_id, date, ticker_symbol, trade_volume, cost_basis)
            db.update_balance(user_id, cash_balance, total)
            if result == True:
                # update the current portfolio holding for total volume of a given stock
                db.update_portfolio_existing(user_id, ticker_symbol, trade_volume)
            else:
                # create a new entry in the portfolio
                db.new_buy_portfolio(user_id, ticker_symbol, trade_volume)

                


def check_balance(user_id, password):
    with Database('terminal_trader.db') as db:
        return db.log_in_information(user_id,password)

        

def sell(user_id, ticker_symbol, trade_volume, cash_balance):
    (ticker_symbol, trade_volume) = view.transaction_menu()
    cost_basis = quote(ticker_symbol)
    date = time(ticker_symbol)
    total = trade_volume * cost_basis
    
    pass

def lookup(company_name):
    #endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
    #response = json.loads(requests.get(endpoint).text)
    #return response
    with Markit() as api:
        return api.lookup(company_name)

def time(ticker_symbol):
    with Markit() as api:
        return api.time_now(ticker_symbol)

def quote(ticker_symbol):
    with Markit() as api:
        return api.quote(ticker_symbol)


if __name__ == '__main__':
    #simple test
    #print('This is the price of Tesla: ', quote(lookup('tesla')))
    user_id = 'Gabby'
    ticker_symbol = 'TSLA'
    trade_volume = 5
    cash_balance = 100000
    print(buy(user_id, cash_balance))



# def lookup_menu():
#     return input('Company Ticker: ')