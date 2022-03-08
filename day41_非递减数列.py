## 给定一个整数数组， 判断在最多改变1个元素的情况下，数组能否变成一个非递减数列

def main():
    each = input('Number:\n')
    stopword = ''
    each1 = each + '\n'
    for line in iter(input, stopword):
        each1 += line + '\n'
    num = each1.splitlines()
    num = list(map(eval, num))

    for i in range(0, len(num)):
        num_copy = num.copy()
        del num_copy[i]     # 改变一个 可以等价转换为 删除一个
        if non_decrease(num_copy) == True:
            return True
    else:
        return False

def non_decrease(seq):
    for i in range(0, len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    else:
        return True

while True:
    print(main())
