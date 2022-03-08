## 给定一个整数数组和一个整数k，找出k-diff数对的个数
## k-diff数对：一个整数对(i, j)，且abs(i-j) = k，i和j都是数组中的数字，(i, j)和(j, i)被算作同一数对

def main():
    nums = []
    k = int(input('Enter k: '))
    while True:
        num = input('Number: ')    # 按两次回车结束输入
        if num == '':
            break
        else:
            nums.append(num)
    print('The array you entered:', nums)
    print('The difference you entered: %d' %k)
    fun(nums, k)

def fun(lis, diff):
    dic = {}
    lis = sorted(list(map(int, lis)))   ##
    
    for i in range(0, lis[-1]-lis[0]+1):
        dic[i] = []

    for i in range(0, len(lis)-1):
        for j in range(i+1, len(lis)):
            dic[lis[j]-lis[i]].append((lis[i], lis[j]))
            
    print('There are %d pairs of numbers meeting the given difference.' %len(set(dic[diff])))   ##
##    for i in set(dic[diff]):
##        print(i, end = ' ')

main()
