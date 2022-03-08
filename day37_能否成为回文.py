## 一个非空字符串s，最多删除一个字符，判断是否能成为回文字符串

from collections import Counter
def main():
    s = list(str(input('Enter a string: ')))
    
    # 每次删除一个字符
    for i in range(0, len(s)):
        s_ = s.copy()
        del s_[i]
        if parlindrome(s_) == True:
##            print(s_, end = '')
            return True
    else:
        return False
    
def parlindrome(string):
    a = 0

    dic = dict(Counter(string))
    lis = list(dic.values())

    if len(set(lis)) == 1:   # 特殊情况：如：aaaa,aaabbb
        return True
    elif len(lis) == 0: # 只针对这道题的特殊情况：空字符串
        return False
    else:               # 普遍情况
        for i in lis:
            if i % 2 == 1:  # 计算奇数次字符，只能出现一次奇数
                a += 1
        if a > 1:   # 如：aaaccdde
            return False
        else:
            return True

print(main())



























