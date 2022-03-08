## 小镇有N个人，其中有一个法官
## 法官不相信任何一个人；其余每个人都信任法官
## 给定数组trust = []，trust[i] = [a,b], 表示a信任b
## 若存在法官且可以确定他的身份，返回代表法官的数字；否则返回-1

def main():
    total = int(input('N = '))
    a, trust = [], []
    count, pos, i = 0, 0, 0
    while True:
        i += 1
        item = input('trust[%d] = ' %i).split(',')
        if len(item) == 1:  # ['']
            break
        else:
            item = list(map(int, item))
            trust.append(item)
            a.append(item[0])
    print('The trust you entered is ', trust)
    for i in range(1, total+1):
        if i not in a:
            count += 1
            pos = i

    if count > 1:
        return -1
    else:
        for i in range(1, total+1):
            if i != pos:
                if [i, pos] not in trust:
                    return -1
        else:
            return pos
print(main())

'''
from collections import Counter

def chancellor(N,trust):
    trusted = [i[1] for i in trust]
    totrust = [i[0] for i in trust]

    cntrst = dict(Counter(trusted))
    cntrst = dict(zip(cntrst.values(),cntrst.keys()))

    chancellor = cntrst[N-1] if cntrst[N-1] not in totrust else -1

    return chancellor

def main():
##    N = int(input('how many people:'))
    N = 3
    trust = [[1,3],[2,3],[3,1]]
    print(chancellor(N,trust))

main()
'''
