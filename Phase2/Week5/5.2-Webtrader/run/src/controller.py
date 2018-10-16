#!/usr/bin/env python3

from mapper.mapper import Database
from flask import Flask, render_template, request, session
import model.model as model

app = Flask(__name__)
app.secret_key = "1234456789"

@app.route('/admin', methods=['GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        session['user_id'] = request.form['user_id']
        password = request.form['password']
        if session['user_id'] == 'Admin' and password == 'Admin':
            return render_template('admin.html')
        else:
            try:
                user_id = model.check_log_in(session['user_id'], password)
                message = "Welcome to your Web Trader homepage {}. What would you like to do?".format(user_id)
                return render_template('dashboard.html', message=message)
            except TypeError:
                message = "Invalid credentials"
                return render_template('login.html', message=message)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if request.method == 'GET':
        return render_template('dashboard.html')




@app.route('/quote', methods=['GET', 'POST'])
def quote():
    if request.method == 'GET':
        return render_template('quote.html')
    elif request.method == 'POST':
        ticker = request.form['ticker']
        if ticker:
            last_price = model.quote(ticker)
            message = "The last price of {} is {}".format(ticker, last_price)
            return render_template('quote.html', message=message)


@app.route('/lookup', methods=['GET', 'POST'])
def lookup():
    if request.method == 'GET':
        return render_template('lookup.html')
    elif request.method == 'POST':
        company = request.form['company_name']
        if company:
            company_name = model.lookup(company)
            message = "The ticker of {} is {}".format(company, company_name)
            return render_template('lookup.html', message=message)   


@app.route('/buy',methods=['GET','POST'])
def buy():
    if request.method == 'GET':
        return render_template('buy.html')
    elif request.method == 'POST':
        user_id = session['user_id']
        ticker_symbol = request.form['ticker']
        trade_volume = int(request.form['volume'])
        cash_balance = model.check_balance(user_id)
        last_price = model.quote(ticker_symbol)
        fee = 6.95
        total = trade_volume * last_price + fee
        trade_result = model.buy(user_id, ticker_symbol, trade_volume)
        if trade_result:
            message = "Success, you have purchased {} shares of {} for {}.".format(trade_volume, ticker_symbol, total)
            return render_template('buy.html', message=message)
        else:
            message = "Your current order of {:.2f} exceeds your cash balance of {:.2f}".format(total, cash_balance)
            return render_template('buy.html', message=message)

        

@app.route('/sell',methods=['GET','POST'])
def sell():
    if request.method == 'GET':
        return render_template('sell.html')
    elif request.method == 'POST':
        user_id = session['user_id']
        ticker_symbol = request.form['ticker']
        trade_volume = int(request.form['volume'])
        cash_balance = model.check_balance(user_id)
        last_price = model.quote(ticker_symbol)
        fee = 6.95
        ticker_status = model.check_ticker_status(user_id, ticker_symbol)
        if ticker_status:
            current_volume = model.current_volume(user_id, ticker_symbol)
            trade_result = model.sell(user_id, cash_balance, ticker_symbol, trade_volume)
            total = last_price * trade_volume
            if trade_result:
                message = "You have succesfully sold {} shares of {} for {:.2f}".format(trade_volume, ticker_symbol, total)
                return render_template('sell.html', message=message)
            else:
                message = "Your requested transaction of {} shares of {} exceeds your current balance of {}".format(trade_volume, ticker_symbol, current_volume)
                return render_template('sell.html', message=message)
        else:
            message = "You do not own any shares of {}".format(ticker_symbol)
            return render_template('sell.html', message=message)


@app.route('/balance',methods=['GET','POST'])
def balance():
    user_id = session['user_id']
    model.update_user_positions(user_id)
    balance = model.check_balance(user_id)
    total_portfolio_value = model.check_total_portfolio(user_id)

    user_positions = model.get_user_positions(user_id)
    tickers = []
    shares = []
    last_price = []
    total_value = []
    position_list = []

    for row in user_positions:
        tickers.append(row[0])
        shares.append(row[1])
        last_price.append(row[2])
        total_value.append(row[3])

    for num in range(0, len(tickers)):
        position_list.append((tickers[num], shares[num], last_price[num], total_value[num]))

    if request.method == 'GET':
        return render_template('balance.html', balance=balance, total_portfolio_value=total_portfolio_value, position_list=position_list )




if __name__ == '__main__':
    app.run("127.0.0.1", port=5001, debug=True)
    