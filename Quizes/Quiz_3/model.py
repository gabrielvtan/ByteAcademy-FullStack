import json
import requests
from pprint import pprint


def get_price():
    ticker = input("Give me a Ticker: ")
    response = requests.get("http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol={}".format(ticker))
    data = response.json()
    return data

