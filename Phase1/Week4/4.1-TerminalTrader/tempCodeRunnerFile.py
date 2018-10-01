#!/user/bin/env python3

import model
import view

def game_loop():
    while 1:
    x = view.main_menu()
    return x

if __name__ == '__main__':
    game_loop()