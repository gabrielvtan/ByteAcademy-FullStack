
from tqdm import tqdm

import model 
import random

for i in tqdm(range(1000000)):
    # random order of doors and generate a winning door
    winning_door = model.index_of_car()

    # random first choice 
    first_choice = model.first_random_choice()

    # select door and receive outcome
    outcome = model.select_door_receive_outcome(first_choice, winning_door)

    # add to database
    #model.add_entry_to_database(winning_door, first_choice, outcome)
