def main():
    a = eval(input('Enter the basic integer: '))
    n = eval(input('Enter the total number of the integer you entered: '))
    s = Sum(a, n)
    print('\nSum of these %d integers is %d.' %(n, s))
    
def Sum(basic, total):
    a_n = 0
    s_n = 0
    for i in range(0, total):
        a_n += basic * 10 ** i
        s_n += a_n
        print(a_n, end = '    ')
    return s_n

main()
