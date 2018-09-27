import sqlite3
from pprint import pprint
from model import Database
import time
import os

school_database = 'school.db'

#done
def add_class():
    os.system('clear')
    print("Please enter the new class entry: ")

def lookup():
    os.system('clear')
    print('What would you like to look-up?')
    lookup_choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n')
    if lookup_choice.upper() == 'C' or 'T' or 'S':
        return lookup_choice
    else:
        print('Incorrect input value')
        time.sleep(2)
        lookup()

def print_database(result):
    os.system('clear')
    print('_________________________')
    print('      DATABASE           ')
    print('_________________________')
    pprint(result)
    time.sleep(4)
    os.system('clear')


def success(entry):
    print('You have successfully created a new {} entry!'.format(entry))
    time.sleep(2)
    os.system('clear')

def error():
    print('Incorrect Entry')
    time.sleep(2)
    os.system('clear')

#done
def add_teacher():
    os.system('clear')
    print("Please enter the new teacher entry: ")

#done
def add_student():
    os.system('clear')
    print("Please enter the new student entry: ")

def exit():
    print('\n\nExiting.....')
    time.sleep(2)
    os.system('clear')
    

