def main():
    global count
    count = 0
    num = input('Nums = ').split(',')
    num = list(map(int, num))
    s = int(input('S = '))
    calcu(num, 0, 0, s)

def calcu(lis, ind, total, s):
    global count
    if ind == len(lis):
        if total == s:
            count += 1
        return None
    else:
        calcu(lis, ind+1, total+lis[ind], s)
        calcu(lis, ind+1, total-lis[ind], s)
        
main()
print(count)
