from pprint import pprint
import random

gameboard = [['0']*7,['0']*7,['0']*7,['0']*7,['0']*7,['0']*7,['0']*7]
ship_row = 5
ship_column = 5

# Print starting grid
print("Battleship: Let's play a game of chance...")
pprint(gameboard)

turn = 0
while turn <=10:
    guess_row = int(input("Guess Row: "))
    guess_column = int(input("Guess Column: "))
    if guess_row == ship_row and guess_column == ship_column:
        print ("DAMN YOU - you have sunk my battleship")
        break
    elif guess_row not in range(7) or guess_column not in range(7):
        print("Ya done fucked up and fired a missle at the land")
    else:
        if turn == 10:
            print("You lose suckkaaaa")
            print("ship row is ", ship_row)
            print("ship column is ", ship_column)
            break
        else:
            turn = turn + 1
            print('Turn: ', turn)
            print("Ya missed me bitch")
            gameboard[guess_row][guess_column] = 'X'
            pprint(gameboard)

