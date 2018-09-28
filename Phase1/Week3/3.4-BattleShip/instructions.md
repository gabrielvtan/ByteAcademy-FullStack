#### Battleship Game

Battleship Game:

In this project you will build a simplified, one-player version of the classic board game Battleship! In this version, there will be a single ship hidden in a random location on a 7x7 grid (this should be a matrix). The player will have 10 guesses to try to sink the ship. Make sure you use print statements to keep your player engaged in the game.

HINT: try using `os.system('clear')` to clear the terminal between inputs
 

#### Classes & Objects (optional)

You might want to create a Gameboard class that stores the grid of squares and the location of ship tiles. Here's a possible set of methods:

* `__init__(self, w, h):
* *    initializes self.tiles, a gameboard with a width and a height given by width and height
    and self.attempts, a count of the number of guesses that have been made on that board

* place_ship(self, x, y, w, h):
* *    makes a rectangle of squares of the gameboard into ship squares

* place_random_ship(self):
* *    uses random.randint to place a random horizontal or vertical ship on the board

* check(self, x, y):
* *    returns the status of a square, empty, ship, ship that's been hit, or empty square that's been guessed

* mark(self, x, y):
* *    mark a square as guessed or hit and increase self.attempts by one


#### Ideas for expanding the game:

*    Add prompts for a second different user to play against the first, one at a time, and have two different boards (one for each user, like the actual game). The game will end when one player guesses correctly.

*    Add prompts for the computer to play as a second user, guessing random coordinate pairs on the grid. The computer and the user should have SEPERATE boards.

*    Multiple Ships

*   Better than random strategy for the computer