def main():
    n = int(input('Enter an integer (>1): '))
    method1(n)
    print('\n\n')
    method2(n)
    
def method1(n):
    for num in range(1, n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:                   #for循环中if条件一直不满足，最后执行else
                print(num, end = '\t')

def method2(n):
    import math
    for num in range(1, n):
        if num > 1:
            for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    break
            else:
                print(num, end = '\t')

main()
