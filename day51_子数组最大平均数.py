## 给定一个数组，找出平均数最大且长度为k的连续子数组，k由用户输入
## 输出该最大平均数

num = [1,12,-5,-6,50,3]
print(num)
k = int(input('k = '))
while k > len(num):
    k = int(input('Error! k = '))
res = {}
for i in range(0, len(num)-k+1):
    res[sum(num[i:i+k]) / k] = num[i:i+k]
print(max(res))
