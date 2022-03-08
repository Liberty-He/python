## 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
## 相邻的节点：下标与上一层结点下标相同或等于上一层结点下标+1的两个结点

import random

row = int(input('How many rows: '))
num = []
for i in range(0, row):
    num.append([])
    for j in range(0, i+1):
        num[i].append(random.randint(1, 11))
for i in num:
    print(i)

length = num[0][0]
ind = 0
sp = []
for i in range(1, row):
    if num[i][ind] > num[i][ind+1]:
        length += num[i][ind+1]
        ind = ind+1
##        print('a',length)
    elif num[i][ind+1] > num[i][ind]:
        length += num[i][ind]
        ind = ind
##        print('b',length)
    else:
        sp.append(num[i][ind])
        
for i in range(0, len(sp)):
    length += sp[i]

print(length)
print(sp)
