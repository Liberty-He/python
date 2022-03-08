def main():
    nums = list(map(int, input('Nums = ').split(',')))
    eachsum = sum(nums) / 3
    ind, true = 0, 0

    while ind < len(nums):
        eachsum -= nums[ind]
        ind += 1
        if eachsum == 0:
            eachsum = sum(nums) / 3
            true += 1

    if true == 3:
        return True
    else:
        return False

print(main())
