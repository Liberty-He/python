## 在所有子序列里找到最大值减最小值等于1的最长的子序列

import random
def sub(arr):
    finish=[]    # the list containing all the subsequences of the specified sequence
    size = len(arr)    # the number of elements in the specified sequence
    end = 1 << size    # end=2**size
    for index in range(end):   
        array = []    # remember to clear the list before each loop
        for j in range(size):
            if (index >> j) % 2:    # this result is 1, so do not have to write ==
                array.append(arr[j])
        # print(array)
        finish.append(array)
    return finish

def main():
##    length = []
##    num = []
##    for i in range(0, 5):
##        num.append(random.randint(1, 5))
    length = {}
    num =[2,5,8 ,1 , 3 , 5 , 7 , 9 , 2 ,10]
    print(num)
    finish = sub(num)
##    print(finish)
    for i in finish:
        if 2 <= len(i) < len(num):
            i = sorted(i)
            if i[-1] - i[0] == 1:
                length[len(i)] = i
                
    if len(length) == 0:
        return None
    else:
        return max(length), length[max(length)]

print(main())
