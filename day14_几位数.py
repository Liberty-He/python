def main():
    num = eval(input('Enter an positive integer which is less than 100,000: '))
    while num >= 100000 or num <= 0 or type(num) != int: 
        num = eval(input('Error! Enter an positive integer again(0 < number < 100,000): '))
    else:
        digits = how_many_digits(num)
        print('\n%d is a %d-digit number.' %(num, digits))
        
        print('\nEach digit of this %d-digit number is' %digits, end = ' ')
        each_digit(num)
        
        print('\n\nThe reverse order output of %d is' %num, end = ' ')
        reverse(num)

def how_many_digits(num):        
    if 1 <= num <= 9:
        return 1
    elif 10 <= num <= 99:
        return 2
    elif 100 <= num <= 999:
        return 3
    elif 1000 <= num <= 9999:
        return 4
    else:
        return 5

def each_digit(num):
    each = num % 10
    if num // 10 != 0:
        each_digit(num//10)
    print(each, end = ' ')
    
def reverse(num):
    each = num % 10
    print(each, end = '')
    if num // 10 != 0:
        reverse(num//10)

main()
