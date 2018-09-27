import random
import sqlite3
import numpy as np

# randomly generate the prize behind a door and shuffle the order
def shuffle_doors():
    doors = ["goat"] * 2 + ["car"]
    random.shuffle(doors)
    return doors

# index of winning door 
def index_of_car(doors):
    winning_door = doors.index('car')
    return winning_door

# randomly select the first choice for range 0-2
def first_random_choice():
    first_choice = random.randrange(3)
    return first_choice

# remove door taking into account first choice and winning door
# Monty will ALWAYS pick a non-car door, thus ultimate choice 
# comes to simply deciding to change or not to change 
def select_door_receive_outcome(first_choice, winning_door, switch):
    doors = [0,1,2]
    doors.remove(first_choice)
    monty_choice = winning_door
    while monty_choice == winning_door:
        monty_choice = np.random.choice(doors)
    doors.remove(monty_choice)

    if switch:
        first_choice = np.random.choice(doors)
    
    if first_choice == winning_door:
        return True
    else:
        return False


    
def add_entry_to_database(winning_door, first_choice, outcome):
    connection = sqlite3.connect('monty_hall.db', check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO monty_hall(
            winning_door, 
            first_choice,
            outcome
            ) VALUES(
            ?,
            ?,
            ?
        ); """, (
            '{}'.format(winning_door),
            '{}'.format(first_choice),
            '{}'.format(outcome)
            )
        )
    
    connection.commit()
    cursor.close()
    connection.close()


