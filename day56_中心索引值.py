def main():
    num = input('Nums = ').split(',')
    num = list(map(int, num))
    for i in range(1, len(num)-1):
        if sum(num[0:i]) == sum(num[i+1::]):
            return i
    else:
        return -1
print(main())
