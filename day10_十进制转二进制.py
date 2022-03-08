def DtoB(num):
    a = num % 2
    if num < 2:
        print(a, end = '')
    else:
        DtoB(num//2)
        print(a, end = '')

DtoB(1)

'''
a1 = 11 % 2
    a2 = 5 % 2
        a3 = 2 % 2        
            a4 = 1 % 2 = 1
            print(a4)
        print(a3)
    print(a2)
print(a1)
'''
