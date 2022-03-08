from numpy import *

n = int(input('Enter n(3, 5, 7...): '))

row = 0
col = n // 2
magic = zeros((n, n))
magic[row][col] = 1

for num in range(2, n*n + 1):
    row_new = (row - 1 + n) % n
    col_new = (col + 1) % n
    
    if magic[row_new][col_new] == 0:
        row = row_new
        col = col_new       
    else:
        row = (row + 1) % n
        
    magic[row][col] = num

print()
print(magic)
