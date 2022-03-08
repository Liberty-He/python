import os

def main():
    n = eval(input('Enter the number of integers: '))
    while type(n) != int:
        n = eval(input('Error! Please enter an integer again: '))
        print( )
    else:
        if n > 0:
            print('Sum of these numbers is %d.' %Sum(n))
        else:
            os._exit(0)

def Sum(total):
    i = 1   #计数器
    sum_num = 0     #初始化和值
    while i <= total:   #输入total个数个整数
        num = eval(input('Enter number %d:' %i))
        while type(num) != int:
            num = eval(input('Error! Enter integer number %d again:' %i))
        else:
            sum_num += num
            i += 1
    return sum_num

main()
