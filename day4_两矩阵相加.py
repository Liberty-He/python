from numpy import *

def main():
    n = int(input('Enter the number of rows: '))
    m = int(input('Enter the number of columns: '))
    Sum = two_matrix(n, m)
    print('\nMatrix A + Matrix B =')
    print(Sum)
    
def two_matrix(row, column):
    A = zeros((row, column))
    B = zeros((row, column))
    C = zeros((row, column))
    
    print('\nMatrix A:')
    for r in range(0, row):
        for c in range(0, column):
            A[r][c] = eval(input('Enter A[%d,%d]: ' %(r, c)))

    print('\nMatrix B:')
    for r in range(0, row):
        for c in range(0, column):
            B[r][c] = eval(input('Enter B[%d,%d]: ' %(r, c)))
                
    for r in range(0, row):
        for c in range(0, column):            
            C[r][c] = A[r][c] + B[r][c]
    return C

main()
            
