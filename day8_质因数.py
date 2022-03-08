def main():
    global factor
    n = int(input('Enter a positive integer: '))
    factor = set()
    prifac(n)
    print('Prime factors of {} are {}'.format(n, factor))
    
def prifac(num):
    for i in range(2, num+1):
        if num % i == 0:
            factor.add(i)
            return prifac(int(num/i))

main()
