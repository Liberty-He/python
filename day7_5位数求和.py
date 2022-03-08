def main():
    n = int(input('Enter an integer : '))
    print(Sum(n))
    
def Sum(num):
    s_n = 0
    if num != 0:
        a_n = num % 10      #取余数，即每一位数
        s_n = a_n + Sum(num//10)    #取整，递归，让每一位数字相加
    return s_n
    
main()

'''字符串数组方法
def Sum_5(Ied):
    if Ied == 0:
        return Ls[0]
    else:
        return Ls[Ied]+Sum_5(Ied-1)

def main():
    global Ls
    num = input('Input the number:')
    Ls = []
    for i in num:
        Ls.append(int(i))
    n = len(Ls)-1
    print('Sum={}'.format(Sum_5(n)))

main()

'''
