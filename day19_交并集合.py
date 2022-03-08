import random
COLUMN = 78    #全局变量，分割线所占列数

##函数入口
# @para None
# @return None
def main():
    print('Set A:')
    A = creat_set()
    display(A)

    print('\nSet B:')
    B = creat_set()
    display(B)

    print('\n\n', 'Union'.center(COLUMN, '='))

    print('Enter the union of A and B')
    print('!! Enter -1 when you want to stop !!\n')
    enter_judge(A | B)

    print('\n\n', 'Insection'.center(COLUMN, '='))

    print('Enter the insection of A and B')
    print('!! Enter -1 when you want to stop !!\n')
    enter_judge(A & B)


##按题目要求创建集合
# @para None
# @return None
def creat_set():
    Set = set()
    total_elements = random.randint(2, 10)
    for i in range(1, total_elements + 1):      #元素个数[1, 10]随机
        Set.add(random.randint(0, 1000))        #元素大小[0, 1000]随机
    return Set


##按题目要求显示集合
# @Set 需要显示的集合
# @return 需要显示的集合
def display(Set):
    column = 0    #局部变量，控制每行数字的个数
    for i in Set:
        print('%5d' %i, end = '')
        column += 1
        if column % 10 == 0:
            print()
    return Set


##输入答案并且判断答案
# @para 两个集合的并集或者交集
# @return 两个集合的并集或者交集
def enter_judge(SetC):
    i = 1
    error = 1
    Set = set()

    # @error 共有三次输入机会
    while error <= 3:
        
        # 输入部分
        print('Try%d: ' %error)
        while True:             ##
            ele = int(input('Element %d: ' %i))
            if ele != -1:
                Set.add(ele)
                i += 1
            else:
                break
            
        # 判断部分 
        if SetC == Set:
            print('Right')
            break
        else:        
            print('Wrong!\n')
            error += 1
            i = 1               #初始化i
            Set = set()         #初始化Set
            
    # 三次机会用完，显示正确答案
    else:
        print('The correct answer: ')
        display(SetC)
        
    return SetC
            
main()


























