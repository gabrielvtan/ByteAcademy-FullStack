from pprint import pprint
import random

#Create classes for the Battleship(User) and the Gameboard
class Battleship:
    """ Ship object container and gameboard"""
    def__init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.tiles = [['#' for i in range(rows)] for i in range(columns)]
        self.attmepts = 0
    
    def place_random_ship(self, row, column):
        self.row = random.randint(0,6)
        self.column = random.randint(0,6)

    def place_ship(self, row, column):
        self.place_ship = (row,column)
    
    def print_board(self):
        for row in self.tiles:
            for tile in row:
                print(tile, end = "")
            print()

    def mark(self, row, column):
        if (row,column) == self.ship_postion:
            

#MAIN LOOP

#while the length of the battleship array is not equal to array of correct guesses
    #Ask for the user input
        #if the guess is incorrect:
            #update the board to include the miss
        #elif the guess has already been selected:
            #print you have already set this position
        #else (the guess is correct:)
            #append the correct guess to the array of correct guesses
            #update the board to include hit

         