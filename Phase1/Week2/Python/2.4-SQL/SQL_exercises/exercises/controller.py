import sqlite3
import os
import time
#import model

while True:
    # runs bash commands
    os.system('clear')
    print('\n\nWhat would you like to add to our DB?')
    choice = input('\n\n[C]lass\n[T]eacher\n[S]tudent\n')
    if choice.upper() == 'C': 
        class_id = input()
    
    elif choice.upper() == 'T':
        pass

    elif choice.upper() == 'S':
        pass

    elif choice.upper() == 'E':
        print('\n\nExiting....')
        break    

    else:
        print('Invalid Choice. Please type C, T, or S')
        #wait a specified amount of seconds
        time.sleep(3)