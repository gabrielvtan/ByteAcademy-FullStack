import random
from tqdm import tqdm
import numpy as np


def select_door_receive_outcome(first_choice, winning_door, switch):
    for _ in tqdm(range(1)):
        doors = [0,1,2]
        print('first door', doors)
        print('first choice', first_choice)
        print('winning', winning_door)
        doors.remove(first_choice)
        print('second door', doors)
        monty_choice = winning_door
        print('Monty1', monty_choice)
        while monty_choice == winning_door:
            monty_choice = np.random.choice(doors)
            print('Monty2', monty_choice)
        doors.remove(monty_choice)
        print('third door', doors)

        if switch:
            first_choice = np.random.choice(doors)
            print('new',first_choice)

        if first_choice == winning_door:
            print(True)
        else:
            print(False)

first_choice = random.randint(0,2)
winning_door = random.randint(0,2)
select_door_receive_outcome(first_choice, winning_door, True)
