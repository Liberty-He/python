## 两个字符串s和t，s比t短，判断s是否为t的子序列
## 字符串子序列是指长字符串删除一些字符后，不改变剩下字符的相对位置形成的新字符串

def judge(short, long):
    n, m = len(short), len(long)
    i = j = 0
    while i < n and j < m:
        if short[i] == long[j]:
            i += 1
        j += 1
    return i == n

def main():
    s = str(input('s: '))
    t = str(input('t: '))
    print(judge(s, t))

main()

'''
s = input('Input string s:')
t = input('Input string t:')

def search(s,t):
    list1 = []
    ind = 0
    p = ''


    for i in s:
        if i == p:
            ind = t.find(i,ind+1)
        else:
            ind = t.find(i, ind)
        if ind == -1:
            return False
        else:
            list1.append(ind)
            p = i


    if sorted(list1) == list1:
        return True
    else:
        return False

print(search(s,t))
'''
