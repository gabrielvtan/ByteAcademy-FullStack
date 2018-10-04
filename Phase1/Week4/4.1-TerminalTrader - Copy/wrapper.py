#!/usr/bin/env python3

import requests

import json


class Markit:
    def __init__(self):
        self.shared_endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2'
        self.lookup_path = '/Lookup/json?input='
        self.quote_path = '/Quote/json?symbol='

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def lookup(self, company_name):
        return json.loads(
            requests.get(
                self.shared_endpoint
                +self.lookup_path
                +company_name
                ).text
        )[0]['Symbol']

    def quote(self, ticker_symbol):
        return json.loads(
            requests.get(
                self.shared_endpoint
                +self.quote_path
                +ticker_symbol
                ).text
        )['LastPrice']

