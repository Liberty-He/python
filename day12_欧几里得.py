def gcd(num1, num2):
    if (num1 % num2) != 0:
        gcd(num2, num1%num2)
    else:
        print('The great common divisor is %d.' %num2)

def main():
    num1 = int(input('Enter number 1: '))
    num2 = int(input('Enter number 2: '))
    if num1 >= num2:
        gcd(num1, num2)
    else:
        gcd(num2, num1)

main()
