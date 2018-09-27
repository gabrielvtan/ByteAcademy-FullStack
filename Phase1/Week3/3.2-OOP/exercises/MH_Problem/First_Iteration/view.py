import time
import os

def main_menu():
    print('\nWelcome to Cars and Goats! Which door would you like to select? ')
    choice = int(input('\n[1] Door\n[2] Door\n[3] Door\n'))
    os.system('clear')
    print("You have Selected door number {}".format(choice))
    return choice

def goat_statement(door_to_remove_, closed_doors):
    print('There is a goat in door {}'.format(door_to_remove_))
    print('The remaining doors are {} and {}.'.format(closed_doors[0], closed_doors[1]))
    final_choice = int(input('Which door would you like to select? '))
    return final_choice

 