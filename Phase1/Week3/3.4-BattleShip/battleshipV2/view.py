from board import Board

import os
import re

MAXTRIES = 100
W = 7
H = 7

def inputxy():
    print("x from 1 to {}, y from 1 to {}.".format(W, H))
    inp = input("Input x,y: ")
    m = re.search("(\d+)[, ]+(\d+)", inp.strip())

    if not m:
        return None, None
    x = int(m.groups()[0])
    y = int(m.groups()[1])
    return x, y

def outputdisplay(board, tries, player):
    os.system('clear')
    print("BATTLESHIP!")
    print("Player Name: {}".format(player))
    print("Hits: {}, Misses: {}, Tries Remaining: {}".format(
            board.hits, board.misses, tries
        ))
    print()
    print(board.display_view())
    print()

def outputloss():
    print("You ran out of tries, you have lost the game.")

def outputwin():
    print("You sunk my battleship!")

def check(board, x, y):
    if not 1 <= x <= W or not 1 <= y <= H:
        return(False, "The coordinates out of range.")
    if not board.check(x-1, y-1) in ("Ship", None):
        return(False, "You already attacked that square.")
    else:
        return (True, "")

def attack(board, x, y):
    board.mark(x-1, y-1)



