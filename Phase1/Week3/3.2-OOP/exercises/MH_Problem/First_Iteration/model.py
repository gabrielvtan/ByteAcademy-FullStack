import random
import os
import time

available_doors = [1,2,3]

# randomly generate the prize behind each door
def generate_prize():
    winning_door = random.choice(available_doors)
    return winning_door

# randomly select which door to remove that is not the winning door
def remove_door(winning_door, choice):
    door_to_remove = random.choice(available_doors)
    if door_to_remove != winning_door and door_to_remove != choice:
        return int(door_to_remove)
    else:
        return remove_door(winning_door,choice)

def winner_or_loser(final_choice, winning_door):
    if final_choice == int(winning_door):
        print('Congrats! You won a car')
    else:
        print('Sorry... You won a goat')

