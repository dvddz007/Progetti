n = 1
while n <= 10:
    for i in range(n, n*10+1, n):
        if i < 10:
            print(' ',end='')
            print(i, end=' ')
        else:
            print(i, end=' ')
    n += 1
    print('')
