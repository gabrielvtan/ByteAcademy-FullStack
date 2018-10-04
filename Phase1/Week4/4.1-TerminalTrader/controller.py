#!/usr/bin/env python3

from mapper import Database

import model
import view
import time


def game_loop(): 
    while True:
        (user_id, password) = view.log_in()
        cash_balance = model.check_balance(user_id, password)

        # input sanitizations
        check_balance_inputs = ['c','C', 'check']
        buy_inputs = ['b', 'B', 'buy']
        sell_inputs = ['s', 'S', 'sell']
        lookup_inputs = ['l', 'L', 'lookup', 'look up']
        quote_inputs = ['q', 'Q', 'quote']
        exit_inputs = ['e', 'exit', 'quit']
        acceptable_inputs = buy_inputs \
                            +sell_inputs \
                            +lookup_inputs \
                            +quote_inputs \
                            +check_balance_inputs \
                            +exit_inputs 
        
        user_input = view.main_menu(user_id)
        if user_input in acceptable_inputs:
            if user_input in buy_inputs:
                model.buy(user_id, cash_balance)
                break
            elif user_input in check_balance_inputs:
                view.check_balance(cash_balance)
                time.sleep(2) 
                break
            elif user_input in sell_inputs:
                model.sell(user_id, cash_balance)
                break
            elif user_input in lookup_inputs:
                return model.lookup(view.lookup_menu())
            elif user_input in quote_inputs:
                return model.quote(view.quote_menu())
            elif user_input in exit_inputs:
                break

 
        

if __name__ == '__main__':
    print(game_loop())