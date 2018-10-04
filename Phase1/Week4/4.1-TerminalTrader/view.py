#!/usr/bin/env python3

import os
import time

def buy_menu():
    os.system('clear')
    print('What stock would you like to purchase?')
    return input('Ticker Symbol: '), int(input('Trade Volume: '))

def check_balance(balance):
    print('Your current cash balance is ', balance)

def error_message():
    print('You have entered an invalid purchase order')
    time.sleep(2)
    os.system('clear')

def header():
    os.system('clear')
    os.system('cowsay -s "Welcome to Terminal Trader -$(whoami)"')

def header_user(user_id):
    os.system('clear')
    print('Welcome {} to Terminal Trader!'.format(user_id))


def log_in():
    header()
    print("Please enter your log-in information: ")
    return input("Username: "), input("Password: ")

def lookup_menu():
    return input('Company name: ')

def main_menu(user_id):
    header_user(user_id)
    print('[C]heck Balance \n[B]uy \n[S]ell \n[L]ook-up \n[Q]uote\n[E]xit')
    return input('\nWhat do you want to do? ')   

def quote_menu():
    return input('Ticker Symbol: ')



