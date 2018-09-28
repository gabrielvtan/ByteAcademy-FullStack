from random import randint

class Board():
    def __init__(self, w, h):
        self.squares = []
        for row in range(h):
            self.squares.append([None for _ in range(w)])
        self.w = w
        self.h = h
        self.hits = 0
        self.misses = 0

    def place_ship(self, values={}):
        horizontal = values.get("horizontal", [True, False][randint(0,1)])

        if horizontal == True:
            x = values.get("x", randint(0, self.w - 4 - 1))
            y = values.get("y", randint(0, self.h - 1))
            for i in range(4):
                self.set(x+i, y, "Ship")
        else:
            x = values.get("x", randint(0, self.w - 1))
            y = values.get("y", randint(0, self.h - 4 - 1))
            for i in range(4):
                self.set(x, y+i, "Ship")

    def check(self, x, y):
        return self.squares[y][x]

    def set(self, x, y, value):
        self.squares[y][x] = value

    def mark(self, x, y):
        if self.check(x, y) == None:
            self.set(x, y, "Miss")
            self.misses += 1

        elif self.check(x, y) == "Ship":
            self.set(x, y, "Hit")
            self.hits += 1

    def display_view(self, view={"Hit": "X", "Miss": "O"}):
        output = ""
        for y in range(self.h):
            rowstring = ""
            for x in range(self.w):
                square = view.get(self.check(x, y), '#')
                rowstring = rowstring + square
            output = output + rowstring + "\n"
        return output

    def allhits(self):
        for x in range(self.w):
            for y in range(self.h):
                if self.check(x, y) == "Ship":
                    return False
        return True

    def __str__(self):
        value = "Board({}, {})\n".format(self.w, self.h)
        value += self.display_view({"Hit": "X", "Miss": "o", "Ship": "@"})
        value += "hits: {}, misses {}".format(self.hits, self.misses)
        return value
