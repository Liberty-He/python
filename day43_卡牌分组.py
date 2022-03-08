## 给定一副牌，每张牌上写着一个整数，输入一个整数X，进行分组
## 每组有X张牌；同一组的牌上写着相同的整数
## 仅当 X >= 2 时能成功分组时，返回true

import random
from collections import Counter

def creat(): 
    deck = []
    for i in range(0, random.randint(2, 20)):
        deck.append(random.randint(0, 5))       
    return deck

def group(deck, x):
    dic = dict(Counter(deck))
    lis = list(dic.values())

    if x >= 2:
        for i in lis:
            if i % x != 0:
                return False
        else:
            return True
    else:
        return False
    
def main():
    deck = creat()
    print('The deck is:', deck)

    x = int(input('Enter x: '))
    
    if group(deck, x) == True:
        return True
    else:
        return False
    
##print(main())
    
print(group([1,2,3,4,4,3,2,1], 2))
print(group([1,1,1,2,2,2,3,3],3))
print(group([1],1))
print(group([1,1],2))

print(group([1,1,2,2,2,2],2))
