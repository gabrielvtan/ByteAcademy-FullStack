import os
import time
from tqdm import tqdm

import model 
import random

doors = ["goat"] * 2 + ["car"]
wins = 0
loses = 0

for i in tqdm(range(100000)):
    # random order of doors
    random.shuffle(doors)

    # random own choice 
    n = random.randrange(3)
    sequence = [0,1,2]
    random.shuffle(sequence)
    for k in sequence:
        if k == n or doors[k] == 'car':
            continue 
    
        if doors[n] == "car":
            loses += 1
        else:
            wins += 1 

print ('Changing has {} wins and {} losses'.format(wins, loses)) 
perc = (100.0 * wins) / (wins + loses)
print("IOW, by changing you win {} of the time".format(perc))