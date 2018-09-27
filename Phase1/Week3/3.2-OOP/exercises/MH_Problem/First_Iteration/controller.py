import os
import time

import view
import model 



def controller():
    closed_doors = [1,2,3]

    # Set initial main menu
    os.system('clear')

    # pick initial door 
    choice = view.main_menu()

    # generate winning door
    winning_door = model.generate_prize()

    # set door to remove based on result and winning door
    door_to_remove_ = model.remove_door(winning_door, choice)
    closed_doors.remove(door_to_remove_)
    final_choice = view.goat_statement(door_to_remove_, closed_doors) 
    model.winner_or_loser(final_choice, winning_door)

controller()
