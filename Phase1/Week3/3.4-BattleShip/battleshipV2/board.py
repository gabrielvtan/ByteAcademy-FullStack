from random import randint

class Board():
    def __init__(self, w, h):
        # create board with dimensions w by h
        # set hits and misses to 0 
        self.squares = []
        for row in range(h):
            self.squares.append([None for _ in range(w)])
        self.w = w
        self.h = h
        self.hits = 0
        self.misses = 0

    # randomly set a ship horizontally or vertically
    # creating a dictionary for the ship placement 
    def place_ship(self, values={}):
        horizontal = values.get("horizontal", [True, False][randint(0,1)])

        if horizontal == True:
            x = values.get("x", randint(0, self.w - 4 - 1))
            y = values.get("y", randint(0, self.h - 1))
            for i in range(4):
                self.set_(x+i, y, "Ship")
        else:
            x = values.get("x", randint(0, self.w - 1))
            y = values.get("y", randint(0, self.h - 4 - 1))
            for i in range(4):
                self.set_(x, y+i, "Ship")

    # Check to see if the is a ship in a given X Y coordinate    
    def check(self, x, y):
        return self.squares[y][x]

    # Set initial ship on the game board
    def set_(self, x, y, value):
        self.squares[y][x] = value

    # Mark the gameboard for hits and misses
    # Increase count for each user
    def mark(self, x, y):
        if self.check(x, y) == None:
            self.set_(x, y, "Miss")
            self.misses += 1

        elif self.check(x, y) == "Ship":
            self.set_(x, y, "Hit")
            self.hits += 1

    # Create a viewable game board at each turn
    def display_view(self, view={"Hit": "X", "Miss": "O"}):
        output = ""
        for y in range(self.h):
            rowstring = ""
            for x in range(self.w):
                square = view.get(self.check(x, y), '#')
                rowstring = rowstring + square
            output = output + rowstring + "\n"
        return output

    # Check to see if the ship has been completely sunk
    def allhits(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.check(x, y) == "Ship":
                    return False
        return True

    # Create key values for hits, misses, ships
    def __str__(self):
        value = "Board({}, {})\n".format(self.w, self.h)
        value += self.display_view({"Hit": "X", "Miss": "o", "Ship": "@"})
        value += "hits: {}, misses {}".format(self.hits, self.misses)
        return value
