import model

def display(data):
    last_price = data['LastPrice']
    symbol = data['Symbol']
    print("The last price of {} is {}".format(symbol, last_price))

