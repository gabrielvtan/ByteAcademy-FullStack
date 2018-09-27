import random
import os
import time
import sqlite3

available_doors = [1,2,3]

# randomly generate the prize behind each door
def generate_prize():
    winning_door = random.choice(available_doors)
    return winning_door

# randomly select which door to remove that is not the winning door
def remove_door(winning_door, first_choice):
    doors = [1,2,3]
    doors.remove(winning_door)
    door_to_remove = random.choice(doors)
    if door_to_remove != first_choice:
        return door_to_remove
    else:
        return remove_door(winning_door,first_choice)

def winner_or_loser(final_choice, winning_door):
    if final_choice == int(winning_door):
        return True
    else:
        return False

def first_random_choice():
    first_choice = random.choice(available_doors)
    return first_choice

def random_choice_after_goat(closed_doors):
    final_choice = random.choice(closed_doors)
    return final_choice
    
def add_entry_to_database(winning_door, first_choice, door_to_remove, final_choice, outcome):
    connection = sqlite3.connect('monty_hall.db', check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(
        """INSERT INTO monty_hall(
            winning_door, 
            first_choice,
            door_to_remove,
            final_choice,
            outcome
            ) VALUES(
            ?,
            ?,
            ?,
            ?,
            ?
        ); """, (
            '{}'.format(winning_door),
            '{}'.format(first_choice),
            '{}'.format(door_to_remove),
            '{}'.format(final_choice),
            '{}'.format(outcome)
            )
        )
    
    connection.commit()
    cursor.close()
    connection.close()


