#!/usr/bin/env python3

### inefficient for-loop
def McNuggets(n):
    Non_McNuggets = []
    McNuggets = []
    for number in range(1, n+1):
        for a in range(0,n):
            for b in range(0,n):
                for c in range(0,n):
                    if 6*a + 9*b + 20*c == number:
                        McNuggets.append(number)
        if number not in McNuggets:
            Non_McNuggets.append(number)      
    return Non_McNuggets


##################################
# more efficient while loop
def McNugg(x):
    McNugg = [0]
    i = 1
    Non_McNugg = []
    while i <= x:
        if (i-6) in McNugg or (i-9) in McNugg or (i-20) in McNugg:
            McNugg.append(i)
            i += 1
        else:
            i += 1 
    for num in range(0, x):
        if num not in McNugg:
            Non_McNugg.append(num)
    return Non_McNugg

print(McNugg(40))