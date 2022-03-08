import os

COLUMN = 78

def main1():
    num = int(input('Enter a positive integer: '))
    if is_prime(num) and is_Mersenne(num):
        print('True')
        return p
    else:
        print('False')
        return -1

def main2():
    '''
    题目要求此行不需要输出
    print('%3s' %'P', end = '\t')
    print('%4s' %'2^P-1')
    '''
    num = 2
    while num <= 1000:
        if is_prime(num) and is_Mersenne(num):
            print('%3d' %p, end = '\t')
            print('%4d' %num)
            num += 1
        else:
            num += 1
            continue

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def is_Mersenne(num):
    global p
    for p in range(1, num):
        if num == 2 ** p -1:
            return True
    else:
        return False

    
def main():
    while True:
        cutting_line = 'Content'
        print(cutting_line.center(COLUMN, '='))
        print('1.Judge the Mersenne prime\n2.Output Mersenne primes less than 1,000\n3.Exit')
        print('=' * COLUMN)
        choose = int(input('Your choice: '))
        if choose == 1:
            main1()
            print('\n')
        elif choose == 2:
            main2()
            print('\n')
        else:
            os._exit(0)
main()
