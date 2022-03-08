def main():
    info = {}
    total = int(input('How many employees: '))    #控制总人数
    print()
    n = 1
    while n <= total:
        name = str(input('Name%d: ' %n))
        number = input('Number%d: ' %n)
        print()
        info[name] = number
        n += 1
        
    print('By name:')
    byname(info)
    print()
    print('By number:')
    bynumber(info)

    
##按姓名顺序
def byname(dic):
    for i in sorted (dic) : 
        print( (i, dic[i]) )
    return dic

    
##按编号顺序
def bynumber(dic):    
    reverse = {v: k for k, v in dic.items()}    #不懂
    for i in sorted(reverse.items(), key = lambda r : r[0]):    #不懂
        print (i)
    return reverse

main()

'''
def sort_name(dict1):
    list1 = dict1.items()
    list1 = sorted( list1,key = lambda x:x[0])
    for i in list1:
        for j in i:
            print(j , end = '\t')
        print()

def sort_num(dict1):
    list2 = dict1.items()
    list2 = sorted( list2,key = lambda x:x[1])
    for i in list2:
        for j in range(1,-1,-1):
            print( i[j] , end = '\t')
        print()

def main():
    dict1 = {}
    n = int(input('How many names to input:'))
    for i in range(n):
        name = input('\nInput the name:')
        num = input('Input the number:')
        dict1[name] = num

        
    print('\nSort by name:')
    sort_name(dict1)

    print('\nSort by number:')
    sort_num(dict1)


main()
'''
