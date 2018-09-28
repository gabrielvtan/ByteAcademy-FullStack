from board import Board
import re
import os

MAXTRIES = 100
W = 7
H = 7

def inputxy():
    print("x from 1 to {}, y from 1 to {}.".format(W, H))
    inp = input("Input x,y: ")
    m = re.search("(\d+)[, ]+(\d+)", inp.strip())
#    print(m.groups())
    if not m:
        return None, None
    x = int(m.groups()[0])
    y = int(m.groups()[1])
    return x, y

def outputdisplay(board, tries):
    os.system('clear')
    print("BATTLESHIP!")
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

#########################


def gameloop():
    board = Board(W, H)
    board.place_ship()
    tries = MAXTRIES

    while True:
        print()
        print()
        outputdisplay(board, tries)

        if board.allhits():
            outputwin()
            break

        if tries <= 0:
            outputloss()
            break

        x, y = inputxy()
        if not x:
            print("Error reading input.")

        if x == 99 and y == 99:
            print(board)
            print("... cheater.")

        else:
            result = check(board, x, y)
            if not result[0]:
                print(result[1])
            else:
                attack(board, x, y)
                attackresult = board.check(x-1, y-1)
                if attackresult == "Miss":
                    tries -= 1

if __name__ == "__main__":
    gameloop()
