#!/usr/bin/env python3

import os

def transaction_menu():
    return input('Ticker Symbol: '), input('Trade Volume: ')

def lookup_menu():
    return input('Company name: ')


def quote_menu():
    return input('Ticker Symbol: ')


def header():
    os.system('clear')
    print('\n* Terminal Trader *\n')
    os.system('cowsay -s "Welcome to Terminal Trader -$(whoami)"')


def main_menu():
    header()
    print('[B]uy \n[S]ell \n[L]ook-up \n[Q]uote\n[E]xit')
    return input('\nWhat do you want to do? ')


