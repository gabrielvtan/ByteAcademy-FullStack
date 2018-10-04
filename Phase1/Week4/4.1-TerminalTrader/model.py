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
            db.new_transction(user_id, date, ticker_symbol, trade_volume, cost_basis)
            db.update_balance(user_id, cash_balance, total)
            if result:
                # update the current portfolio holding for total volume of a given stock
                db.update_portfolio_existing(user_id, ticker_symbol, trade_volume)
            else:
                # create a new entry in the portfolio
                db.new_buy_portfolio(user_id, ticker_symbol, trade_volume)



def check_balance(user_id, password):
    with Database('terminal_trader.db') as db:
        return db.log_in_information(user_id,password)

        

def sell(user_id, cash_balance):
    # cost_basis is actually sale price
    (ticker_symbol, trade_volume) = view.sell_menu()
    cost_basis = quote(ticker_symbol)
    date = time(ticker_symbol)
    with Database('terminal_trader.db') as db:
        result = db.check_ticker_status(user_id, ticker_symbol)
        current_volume = int(db.check_volume(user_id, ticker_symbol))
        if trade_volume > current_volume:
            view.error_message()
            sell(user_id, cash_balance)
        else:
            trade_volume = -trade_volume
            total = cost_basis * trade_volume
            # record the transaction in transactoins table
            db.new_transction(user_id, date, ticker_symbol, trade_volume, cost_basis)
            # decrease volume in portfolio table
            db.update_portfolio_existing(user_id, ticker_symbol, trade_volume)
            # increase the cash balance 
            db.update_balance(user_id, cash_balance, total)

    

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
    #ticker_symbol = 'TSLA'
    #trade_volume = 5
    cash_balance = 100000
    print(sell(user_id, cash_balance))



# def lookup_menu():
#     return input('Company Ticker: ')