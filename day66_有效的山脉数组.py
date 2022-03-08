def main():
    nums = list(map(int, input('Nums: ').split(',')))
    if is_only(nums):
        ind = nums.index(max(nums))
        if ind == len(nums) - 1 or ind == 0:
            return False
        else:
            left = nums[0:ind]
            right = nums[ind+1::]
            if left == sorted(list(set(nums[0:ind]))) and right == sorted(list(set(nums[ind+1::])), reverse = True):
                return True
            else:
                return False
    else:
        return False

def is_only(lis):
    total = lis.count(max(lis))
    if total == 1:
        return True
    else:
        return False

print(main())
