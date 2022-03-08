## 两个没有重复元素的数组nums1和nums2，nums1是nums2的子集，找到nums1中每个元素在nums2中的下一个比其大的值
## nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素（不一定相邻），如果不存在，对应位置输出-1

import random
nums1 = random.sample(range(1, 6), 3)
nums2 = random.sample(range(1, 6), 5)
print('nums1 =', nums1, '\nnums2 =', nums2)

res = []
for i in range(0, len(nums1)):
    for j in range(0, len(nums2)):
        if nums1[i] == nums2[j] and j != len(nums2)-1:
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums2[j]:
                    res.append(nums2[k])
                    break
            else:
                res.append(-1)
            break
        elif j == len(nums2)-1:
            res.append(-1)
print(res)
