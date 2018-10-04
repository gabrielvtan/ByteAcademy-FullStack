#!/usr/bin/env python3

from mapper import Database
#import wrapper
from wrapper import Markit

import requests
import json

def buy(user_id, ticker_symbol, trade_volume):
    with Database('master.db') as db:
        pass

    with Markit() as m:
        quote = m.quote(ticker_symbol)
    

def sell():
    pass

def lookup(company_name):
    #endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
    #response = json.loads(requests.get(endpoint).text)
    #return response
    with Markit() as m:
        return m.lookup(company_name)

def quote(ticker_symbol):
    with Markit() as m:
        return m.quote(ticker_symbol)


if __name__ == '__main__':
    with Database('master.db') as db:
        db.create_table('users')
        db.create_table('orders')
        db.create_table('holdings')
        db.add_column('users', 'username', 'VARCHAR')
        db.add_column('users', 'password', 'VARCHAR')
        db.add_column('users', 'balance', 'FLOAT')
        db.add_column('orders', 'ticker_symbol', 'VARCHAR')
        db.add_column('orders', 'trade_volume', 'FLOAT')
        db.add_column('orders', 'execution_price', 'FLOAT')
        db.add_column('holdings', 'ticker_symbol', 'VARCHAR')
        db.add_column('holdings', 'trade_volume', 'FLOAT')
        db.add_column('holdings', 'vwap', 'FLOAT')
        print('System Agent: Database created')
        


# def lookup_menu():
#     return input('Company Ticker: ')