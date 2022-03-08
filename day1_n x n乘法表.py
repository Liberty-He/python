n = int(input('Enter n:'))
for row in range(1, n+1):
    for column in range(1, row+1):
            print('%d' %(row*column), end = '\t')
    print('\n')
