
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


print(McNuggets(40))
