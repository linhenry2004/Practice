for i in range(1, 10):
    for j in range(1, 10):
        result = j * i
        print('%d * %d = %d' % (j, i , result), end = '\t')
        if j == 9: 
            print('\n', end = '')