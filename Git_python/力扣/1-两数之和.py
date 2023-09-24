def twoSum(nums, target):
    a = len(nums)
    for i in range(a):
        for j in range(i + 1, a):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([2, 7, 11, 15], 22))
