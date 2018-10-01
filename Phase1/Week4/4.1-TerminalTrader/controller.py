#!/usr/bin/env python3

import model
import view

def game_loop():
    while 1:
        option_1 = view.main_menu()
        if option_1 == 'l':
            company_name = view.lookup_menu()
            return model.lookup(company_name)

if __name__ == '__main__':
    print(game_loop())