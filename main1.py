for i in range(1,10):
    for j in range(1,10):
        if j >= i:
            F = '{:1}X{:1}={:<2}'.format(i, j, i*j)
        else:
            F = '      '
        print(F,end = ' ')
    print()