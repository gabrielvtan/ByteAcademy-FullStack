#!/usr/bin/env python3

import os

def lookup_menu():
    return input('Company name: ')


def header():
    print('Welcome to Terminal Trader')
    os.system('cowsay -d "fuck you -$(whoami)"')


def main_menu():
    header()
    print('[B]uy \n[S]ell \n[L]ook-up \n[Q]uote')
    return input('What do you want to do? ')


