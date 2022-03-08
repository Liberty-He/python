import random

TOTAL = 1000

def draw():
    first, second, third = 0, 0, 0

    for person in range(1, TOTAL+1):
        i = random.random()

        if 0 <= i < 0.08:
            first += 1
            #print('Person %4d: The FIRST  prize!' %person)

        elif 0.08 <= i < 0.3:
            second += 1
            #print('Person %4d: The SECOND prize!' %person)

        else:
            third += 1
            #print('Person %4d: The THIRD  prize!' %person)
            
    print('一等奖：%3d个' %first)
    print('二等奖：%d个' %second)    
    print('三等奖：%d个' %third)    
    
    return first, second, third

draw()
