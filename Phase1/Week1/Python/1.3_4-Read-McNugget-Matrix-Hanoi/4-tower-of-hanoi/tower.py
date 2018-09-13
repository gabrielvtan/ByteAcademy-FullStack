
A = [3, 2, 1]
B = []
C = []

def move_stack(n, start, stop, middle):
    if n > 0: 
        # move n-1 disks from start to middle
        move_stack(n-1, start, middle, stop)

        # move the nth disk from start to stop
        stop.append(start.pop())

        print(A, B, C, '--------------------', sep = '\n')

        # move the n-1 disks that were on middle onto stop
        move_stack(n-1, middle, stop, start)
        

if __name__ == "__main__":
    move_stack(3, A, B, C)
