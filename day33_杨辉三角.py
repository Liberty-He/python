from numpy import zeros

def main():
    global last_col
    n = int(input('How many rows :(>=3) '))
    if n % 2 == 0:
        last_col = 2*n
        n += 1        
        matrix(n)
        display(n-1)
    else:
        last_col = 2*n-1
        matrix(n)
        display(n)

def matrix(n):
    global res
    res = zeros((n, 2*n-1))
    first = n - 1
    res[0][n-1] = 1
    res[1][n-2] = 1
    res[1][n] = 1

    for row in range(2, n):         
        res[row][n - row - 1] = 1
        res[row][-(n - row)] = 1
        for col in range(first, 2*n-3, 2):
            res[row][col] = res[row-1][col-1] + res[row-1][col+1]
        first -= 1
    return res

def display(n):
    for i in range(0, n):
        for j in range(0, last_col):
            if res[i][j] != 0:
                print(int(res[i][j]), end = ' ')
            else:
                print(' ', end = ' ')        
        print()

main()

'''
n = 7
list1 = []

for i in range(1,n+1):
    row =[]
    for ele in range(i):
        row.append(1)
    list1.append(row)

for row in range(len(list1)):
    for j in range(1,len(list1[row])-1):
        list1[row][j] = list1[row-1][j-1] + list1[row-1][j]

for row in range(1,len(list1)+1):
    print(' ' * (n-row),end = '')
    for ele in list1[row-1]:
        print(ele,end = ' ')
    print()
'''
