#
# https://leetcode.com/problems/maximum-subarray/
#

#
# Kadane's algorithm
#

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray_sum(nums):
        n = len(nums)
        if n == 0:
            return 0
        
        max_current = max_seen = nums[0]
        #
        # max_current represents max array sum possible at that index
        #
        # when we encounter a new element, there are two possibilities,
        #
        # that new element auguments existing max_current (or) new element
        # itself is greater than max_current + element value.ArithmeticError
        #
        # example for 1st scenario,
        #
        # max_current = 2, element = 3 -> here, element auguments existing
        # max_current, hence, new max_current = 2 + 3 = 5
        # 
        # example for 2nd scenario,
        #
        # max_current = -2, element = 3 -> here, element itself adds more
        # value than max_current + element. That is, 3 > -2 + 3
        # hence, max_current = 3
        #
        # so, if new element overpowers previous max_current + current
        # element, then, this new element becomes max_current, since
        # we want the highest max at each index for max_current
        #
        for i in range(1, n):
            max_current = max(max_current + nums[i], nums[i])
            max_seen = max(max_seen, max_current)
        return max_seen
    
        #
        # similar DP approach
        #
        # n = len(nums)
        # if n == 0:
        #     return 0
        #
        # dp = {}
        # maxval = dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i - 1] + nums[i], nums[i])
        #     maxval = max(dp[i], maxval)
        #         
        # return maxval 

print(max_subarray_sum(nums))
