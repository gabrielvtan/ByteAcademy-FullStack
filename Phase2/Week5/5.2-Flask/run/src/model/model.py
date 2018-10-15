#!/usr/bin/env python3

database = 'web_trader.db'

from flask import Flask, render_template, request, session
from wrapper.api import Markit
from mapper.mapper import Database

def quote(ticker_symbol):
    with Markit() as api:
        return(api.quote(ticker_symbol))

def lookup(company_name):
    with Markit() as api:
        ticker = api.lookup(company_name)
        return ticker

def time(ticker_symbol):
    with Markit() as api:
        return api.time_now(ticker_symbol)

def check_balance(user_id):
    with Database(database) as db:
        balance = round(db.cash_balance(user_id), 2)
        return balance

def check_ticker_status(user_id, ticker_symbol):
    with Database(database) as db:
        return db.check_ticker_status(user_id, ticker_symbol)


def current_volume(user_id, ticker_symbol):
    with Database(database) as db:
        return int(db.check_volume(user_id, ticker_symbol))


def buy(user_id, ticker_symbol, trade_volume):
    date = time(ticker_symbol)
    cash_balance = check_balance(user_id)
    last_price = quote(ticker_symbol)
    fee = 6.95
    total = trade_volume * last_price + fee
    if total > cash_balance:
        return False
    else:
        with Database (database) as db:
            result = db.check_ticker_status(user_id, ticker_symbol)
            db.new_transction(user_id, date, ticker_symbol, trade_volume, last_price)
            db.update_balance(user_id, cash_balance, total)
            if result:
                # update the current portfolio holding for total volume of a given stock
                db.update_portfolio_existing(user_id, ticker_symbol, trade_volume, last_price)
                return True
            else:
                # create a new entry in the portfolio
                db.new_buy_portfolio(user_id, ticker_symbol, trade_volume, last_price)
                return True

def sell(user_id, cash_balance, ticker_symbol, trade_volume):
    date = time(ticker_symbol)
    last_price = quote(ticker_symbol)
    with Database(database) as db:
        current_volume = int(db.check_volume(user_id, ticker_symbol))
        if trade_volume > current_volume:
            return False
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
            return True