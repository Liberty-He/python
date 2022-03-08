## 给定一个字符串（区分大小写），找到通过这些字母能构造出的最长回文串（不用输出），输出最长回文串的长度

from collections import Counter
s = str(input('Enter a string consisting of uppercase and lowercase letters.\n'))
length = 0

# 统计每个字符的出现次数
dic = dict(Counter(s))
lis = list(dic.values())

# 计算最长回文长度    
if len(lis) == 1:   # 特殊情况：字符串只由一种字符组成
    length = lis[0]
else:   # 普遍情况
    for i in lis:
        if i != 1:
            if i % 2 == 0:
                length += i
            elif i % 2 == 1:
                length += i-1
    if 1 in lis:
        length += 1
    
print('The maximum length of the palindrome string is %d.' %length)
