19##「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
## 如果可以变为1，那么这个数就是快乐数。
## 如果 n 是快乐数就返回 True ；不是，则返回 False 。
def main():
    num = list(map(int, list(input('Num = '))))
    try:
        if is_happy(num):
            return True
    except RecursionError:
        return False
    
    
def is_happy(lis):
    square = 0
    res = 0
    
    for i in range(0, len(lis)):
        square += lis[i]**2
    if square == 1:
        return True
    else:
        res = list(map(int, list(str(square))))
        return is_happy(res)
print(main())
