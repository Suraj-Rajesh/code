#
# https://leetcode.com/problems/two-sum/
#

def twoSum(nums, target):
    n = len(nums)
    if n <= 1:
        return []

    seen = {nums[0]: 0}
    for i in range(1, len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[nums[i]] = i


print(twoSum([2,7,11,15], 9))
