import os
COLUMN = 78

def main1():
    num = int(input('Enter a positive integer: '))
    if is_prime(num) and not_palindrome(num) and is_prime(num_copy):
        print('%d is an inverse prime number！' %num)
    else:
        print('%d isn\'t an inverse prime number！' %num)
        
def main2():
    num = 1
    n = 0
    while n < 30:
        if is_prime(num) and not_palindrome(num) and is_prime(num_copy):
            print('%5d' %num, end = '\t')
            num += 1
            n += 1
            if n % 8 == 0:
                print()
        else:
            num += 1
            continue
        
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True
    
def not_palindrome(num):
    global num_copy
    
    list_each_digit = []
    num_copy = num       ##
    n = 0
    
    while num_copy != 0:
        list_each_digit.append(num_copy % 10)
        num_copy //= 10

    ## num_copy = 0   
    for each_digit in list_each_digit[::-1]:
        num_copy = num_copy + each_digit * 10 ** n
        n += 1                                      ##201 [1, 0, 2] -> 102
        print(num_copy)

    if num_copy == num:
        return False
    else:
        return True

def main():
    while True:
        cutting_line = 'Content'
        print(cutting_line.center(COLUMN, '='))
        print('1.Judge the inverse prime number\n2.Output the first 30 inverse prime numbers\n3.Exit')
        print('=' * COLUMN)
        choose = int(input('Your choice: '))
        if choose == 1:
            main1()
            print('\n')
        elif choose == 2:
            main2()
            print('\n\n')
        else:
            os._exit(0)
            
not_palindrome(201)
