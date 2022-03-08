def main():
    n = int(input('How many items: '))
    for i in range(1, n+1):
        print(fibo(i), end = '\t')

#求斐波那契数列的第i项   
def fibo(i):
    if i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return ( fibo(i-1) + fibo(i-2) )

main()
        
