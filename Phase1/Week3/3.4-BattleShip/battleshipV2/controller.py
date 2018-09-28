from board import Board
import view

import time

MAXTRIES = 100
W = 7
H = 7

def gameloop():
    player1 = input("Player 1: What is your name? ")
    player2 = input("Player 2: What is your name? ")

    
    board1 = Board(W, H)
    board1.place_ship()

    board2 = Board(W,H)
    board2.place_ship()

    tries1 = MAXTRIES
    tries2 = MAXTRIES

    while True:
        # Controller for player 1 #

        # Print out Player 1 board
        print("\n")
        view.outputdisplay(board1, tries1, player1)

        # If Player 1 sinks Player 2's board, they win
        if board1.allhits():
            view.outputwin()
            break

        # If Player 1 runs out of tries, they lose
        if tries1 <= 0:
            view.outputloss()
            break

        # Get input from player 1
        x1, y1 = view.inputxy()
        if not x1:
            print("Error reading input.")

        # View ship placement for player 1
        if x1 == 99 and y1 == 99:
            print(board1)
            print("... cheater.")
            time.sleep(3)

        # Player 1 checks to see if there is a hit or miss
        else:
            result = view.check(board1, x1, y1)
            if not result[0]:
                print(result[1])
            else:
                view.attack(board1, x1, y1)
                attackresult = board1.check(x1-1, y1-1)
                if attackresult == "Miss":
                    tries1 -= 1

        # Controller for player 2 #

        # Print out Player 2 board
        print("\n")
        view.outputdisplay(board2, tries2, player2)

        # If Player 2 sinks Player 1's board, they win
        if board2.allhits():
            view.outputwin()
            break

        # If player 2 runs out of tries, they lose
        if tries2 <= 0:
            view.outputloss()
            break

        # Get input from player 2
        x2, y2 = view.inputxy()
        if not x2:
            print("Error reading input.")

        # View ship placement for player 2
        if x2 == 99 and y2 == 99:
            print(board2)
            print("... cheater.")
            time.sleep(3)

        # Player 2 checks to see if there is a hit or miss
        else:
            result = view.check(board2, x2, y2)
            if not result[0]:
                print(result[1])
            else:
                view.attack(board2, x2, y2)
                attackresult = board2.check(x2-1, y2-1)
                if attackresult == "Miss":
                    tries2 -= 1


if __name__ == "__main__":
    gameloop()
