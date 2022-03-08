## 给定一个整数数组，需找一个连续子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序
## 这个连续子数组应该是最短的，输出它的长度

import random as r
##num = [2,6,4,8,10,9,15]
num = [1,3,3,2,5]
##num = []
##for i in range(0, 6):
##    num.append(r.randint(1, 4))
print(num)

index = []
num_ = sorted(num)

if num == num_:
    print(len(num))
else:
    for i in range(0, len(num)):
        if num[i] != num_[i]:
            index.append(i)
    print(index[-1] - index[0] + 1)

##[1,3,3,2,5]
##[1,2,3,3,5]
