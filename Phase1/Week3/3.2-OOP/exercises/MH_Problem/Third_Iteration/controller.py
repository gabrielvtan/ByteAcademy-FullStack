import os
import time
from tqdm import tqdm

import view
import model 

def controller():
    
    for i in tqdm(range(100000)):
        closed_doors = [1,2,3]
        os.system('clear')

        # pick initial door 
        first_choice = model.first_random_choice()

        # generate winning door
        winning_door = model.generate_prize()

        # set door to remove based on result and winning door
        door_to_remove = model.remove_door(winning_door, closed_doors)
        closed_doors.remove(door_to_remove)
        final_choice = model.random_choice_after_goat(closed_doors)
        outcome = model.winner_or_loser(final_choice, winning_door)
        #model.add_entry_to_database(winning_door, first_choice, door_to_remove, final_choice, outcome)    

controller()
