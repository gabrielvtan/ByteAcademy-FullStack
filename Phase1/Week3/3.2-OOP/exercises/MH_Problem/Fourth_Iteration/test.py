import numpy as np
from tqdm import tqdm

def monty_hall (num_doors, trials, switch):
    successes = 0
    for _ in tqdm(range(trials)):
        # determine behind which door the prize is
        doors = list(range(1, num_doors+1))
        prize_door = np.random.choice(doors)
        print('first door', doors)
        print(prize_door)

        # door the guest chooses. (Fixed to 1)
        guest_choice = np.random.choice(doors)
        print(guest_choice)
        doors.remove(guest_choice)
        print('second', doors)

        # determine which door the host opens before guest is allowed to switch
        # this will be faster for larger lists than copying the `doors` list
        host_choice = prize_door
        print("host-choice:1", host_choice)
        while host_choice == prize_door:
            host_choice = np.random.choice(doors)
            print("host-choice:2", host_choice)
        doors.remove(host_choice)
        print('third', doors)

        # determine which door the guest chooses if switching
        if switch:
            guest_choice = np.random.choice(doors)

        # check win condition
        if guest_choice == prize_door:
            successes += 1
    return successes / trials

print(monty_hall(3,1,True))