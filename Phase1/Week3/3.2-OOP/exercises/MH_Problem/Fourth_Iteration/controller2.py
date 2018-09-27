import os
import time
from tqdm import tqdm

import model 
import random

wins = 0
loses = 0

for i in tqdm(range(1000000)):
    # random order of doors and generate a winning door
    doors = model.shuffle_doors()
    winning_door = model.index_of_car(doors)

    # random first choice 
    first_choice = model.first_random_choice()

    # select door and receive outcome
    outcome = model.select_door_receive_outcome(first_choice, winning_door, True)
    
    # add to database
    #model.add_entry_to_database(winning_door, first_choice, outcome)
