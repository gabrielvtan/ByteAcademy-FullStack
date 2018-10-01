import view
import model

def ticker_price():
    data = model.get_price()
    last_price = view.display(data)

ticker_price()

