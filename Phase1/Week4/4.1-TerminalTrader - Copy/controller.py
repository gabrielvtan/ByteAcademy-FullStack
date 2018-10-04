#!/usr/bin/env python3

import model
import view
import time

def game_loop():
    while True:
        # input sanitization
        buy_inputs = ['b', 'B', 'buy']
        sell_inputs = ['s', 'S', 'sell']
        lookup_inputs = ['l', 'L', 'lookup', 'look up']
        quote_inputs = ['q', 'Q', 'quote']
        exit_inputs = ['e', 'exit', 'quit']
        acceptable_inputs = buy_inputs \
                            +sell_inputs \
                            +lookup_inputs \
                            +quote_inputs \
                            +exit_inputs 
        
        user_input = view.main_menu()
        if user_input in acceptable_inputs:
            if user_input in buy_inputs:
                (ticker_symbol, trade_volume) = view.transaction_menu()
                confirmation_message = model.buy(ticker_symbol, trade_volume)
                pass

            elif user_input in sell_inputs:
                pass

            elif user_input in lookup_inputs:
                return model.lookup(view.lookup_menu())
            
            elif user_input in quote_inputs:
                return model.quote(view.quote_menu())
            
            elif user_input in exit_inputs:
                break


        

if __name__ == '__main__':
    print(game_loop())