## 给定一个花坛（表示为一个数组包含0和1，0表示没种花，1表示种了花），再给定一个数n
## 若能种入n朵花返回True；否则返回False
## 种花规则：1不能挨着出现

def main():
    print('Please enter the number of flowers \'n\' and flowerbed.')
    print('Each number in flowerbed is separated by \',\'')
    print('For example: flowerbed = 1,0,1,0')

    flowerbed = input('\nfloewrbed = ').split(',')
    n = int(input('n = '))
    flowerbed = list(map(int, flowerbed))
    
    while judge(flowerbed) == False:
        flowerbed = input('Illegal! Enter again! flowerbed = ').split(',')
        flowerbed = list(map(int, flowerbed))
    print(plant(flowerbed, n))

def plant(flowerbed, n):
    count = 0
    
    if flowerbed[0] == flowerbed[1] == 0:
        count += 1
        flowerbed[0] = 1
    if flowerbed[-1] == flowerbed[-2] == 0:
        count += 1
        flowerbed[-1] = 1
    for i in range( 1, len(flowerbed)-1 ):
        if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
            count += 1
            flowerbed[i] = 1
            
    if count >= n:
        return True
    else:
        return False

def judge(flowerbed):
    for i in range( 0, len(flowerbed)-1 ):
        if flowerbed[i] == flowerbed[i+1] == 1:
            return False
    else:
        return True
    
main()

