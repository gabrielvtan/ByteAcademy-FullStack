
def push_zeros(x, n):
    count = 0
    for i in range(n):
        if x[i] != 0:
            x[count] = x[i]
            count += 1
    while count < n:
        x[count] = 0
        count += 1



if __name__ == '__main__':
    x = [0,1,0,3,12]
    n = len(x)
    push_zeros(x,n)
    print(x)
