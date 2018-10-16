"""
You don't need to pay specific attention to the logic handling the data, just know
that position_list is a list of tuples, each corresponding to a position we hold.
"""


@app.route('/portfolio/', methods=['GET', 'POST'])
def portfolio():
    balance = model.check_balance()
    #Returns a float for balance from model

    x = model.view_portfolio()
    #Returns a tuple from a SQL fetchall, one tuple for each position

    names = []
    num_shares = []
    shares_value = []
    position_list = []
    #Initialize empty list for our data

    shares=0
    #Number of total shares I own across all stocks (not necessary)
    for row in x:
        shares += row[2]
        num_shares.append(row[2])
        b = model.portfolio_value(row[1], row[2])
        name.append(b[0])
        shares_value.append(b[1])

    net_bal = round((balance-25000), 2)
    #Round our balance to 2 decimal places, and subtract our starting amount of money

    for num in range(0, len(names)):
        #Length is equal to number of positions we hold
        position_list.append((names[num], num_shares[num], shares_value[num]))
        #List of tuples organized with all the data we want, each tuple is a stock
        #Looks like [(TICKER, SHARES, TOTAL_VALUE), (TICKER, SHARES, TOTAL_VALUE)]
    if request.method == 'GET':
        #Pass lists to jinja
        return render_template('portfolio.html', balance=balance, net_bal=net_bal, shares=shares, position_list=position_list)