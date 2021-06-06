#
# https://leetcode.com/problems/range-sum-query-immutable/
#

a = [1, 2, 3]

class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        #
        # introducing an extra initial element initialized to 0, to avoid
        # checking if left == 0 during sumRange()
        #
        self.sums = [0] * (n + 1)
        for i in range(n):
            self.sums[i + 1] += self.sums[i] + nums[i]

        #
        # self.sums = [0]
        # for i in range(n):
        #     self.sums.append(self.sums[-1] + nums[i])
        #

    def sumRange(self, left, right):
        return self.sums[right + 1] - self.sums[left]

n = NumArray(a)
print(n.sumRange(0, 2))
