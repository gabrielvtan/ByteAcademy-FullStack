import json
from pprint import pprint

file = 'currency.txt'

def readcurrency(file):
    list_of_currency = []
    with open(file, 'r') as open_file: 
        for line in open_file:
            key, value = line.split()
            currency = {"symbol": key, "rate": value}
            list_of_currency.append(currency)
    return list_of_currency

pprint(readcurrency(file))