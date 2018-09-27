import json
import requests

class Wrapper:

    def __init__(self):
         self.base_url = 'http://dev.markitondemand.com/MODApis/Api/v2/'
         self.quote_url = 'Quote/json?symbol='
         self.lookup_url = 'Lookup/json?input='

    def quote(self, symbol):
        api_call = self.base_url + self.quote_url + symbol
        response = json.loads(requests.get(api_call).text)
        last_price = response['LastPrice']
        return last_price

    def lookup(self, company_name):
        api_call = self.base_url + self.lookup_url + company_name
        response = json.loads(requests.get(api_call).text)
        symbol = response[0]['Symbol']
        return symbol
