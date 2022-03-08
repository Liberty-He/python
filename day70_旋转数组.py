nums = list(map(eval, input('Nums = ').split(',')))
k = int(input('k = '))
if k != 0:
    for i in nums[:-k-1:-1]:
        nums.insert(0, i)
    del nums[-k::]
print(nums)
