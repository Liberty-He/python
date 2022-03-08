## 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

## 注意：请不要在超过该数组长度的位置写入元素。

## 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。

def main():
    s = [1,0,2,3,0,4,5,0]
##    s = [1,2,3,0]
    count, i = 0, 0
    while i < len(s):
        if s[i] == 0:
            s.insert(i, 0)
            del s[-1]
            i += 2
            count += 1
        else:
            i += 1
    if count == 0:
        print('null')
    else:
        print(s)
main()

