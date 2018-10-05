#!/usr/bin/env python3

from mapper import Database

import model
import view
import time


def game_loop(): 
    (user_id, password) = view.log_in()
    if user_id == 'Admin' and password == 'Admin':
        while True:

            table_view_inputs = ['t', 'T', 'table']
            leaderboard_inputs = ['l','L','leaderboard']
            exit_inputs = ['e','E', 'exit', 'quit']
            acceptable_inputs = table_view_inputs \
                                + leaderboard_inputs \
                                + exit_inputs

            user_input = view.admin_menu(user_id)
            if user_input in acceptable_inputs:
                if user_input in table_view_inputs:
                    table_name = view.table_view()
                    model.view_table(table_name)
                    time.sleep(5)
                elif user_input in leaderboard_inputs:
                    model.leaderboard()
                    time.sleep(5)
                elif user_input in exit_inputs:
                    break
            else:
                view.error_message()

    else:
        cash_balance = model.check_balance(user_id, password)
        while True:

            check_balance_inputs = ['c','C', 'check']
            buy_inputs = ['b', 'B', 'buy']
            sell_inputs = ['s', 'S', 'sell']
            lookup_inputs = ['l', 'L', 'lookup', 'look up']
            quote_inputs = ['q', 'Q', 'quote']
            exit_inputs = ['e','E', 'exit', 'quit']
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
                    time.sleep(1) 
                elif user_input in check_balance_inputs:
                    view.check_balance(cash_balance)
                    time.sleep(1) 
                elif user_input in sell_inputs:
                    model.sell(user_id, cash_balance)
                elif user_input in lookup_inputs:
                    model.lookup(view.lookup_menu())
                    time.sleep(1) 
                elif user_input in quote_inputs:
                    view.current_price(model.quote(view.quote_menu()))
                    time.sleep(1)
                elif user_input in exit_inputs:
                    break
            else:
                view.error_message()


 
        

if __name__ == '__main__':
    game_loop()