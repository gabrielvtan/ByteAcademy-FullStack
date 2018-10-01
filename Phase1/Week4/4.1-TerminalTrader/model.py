#!/usr/bin/env python3

import mapper 
import wrapper

import requests
import json

def lookup(company_name):
    endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input='+company_name
    response = json.loads(requests.get(endpoint).text)
    return response

def lookup_menu():
    return input('Company Ticker: ')