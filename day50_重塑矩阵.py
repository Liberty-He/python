def fill(num, row, col):
    res = []
    for r in range(0, len(num), col):
        res.append(num[r:r+col])
    return res

def main():
    row = int(input('How many rows: '))
    col = int(input('How many columns: '))
    num = []
    for i in range(1, row + 1):
        for j in range(1, col+1):
            num.append(eval(input('Num[%d][%d]: ' %(i, j))))
            
    num1 = fill(num, row, col)
    print('The array you entered:\n', num1)

    new_row = int(input('\n\nThe new rows: '))
    new_col = int(input('The new columns: '))            
    if row * col == new_row * new_col:
        num2 = fill(num, new_row, new_col)
        print('Result:\n', num2)
    else:
        print('Result:\n', num1)

main()
