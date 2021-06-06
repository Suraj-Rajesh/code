#
# https://leetcode.com/problems/find-the-duplicate-number/
#

def findDuplicate(nums):
    #
    # Approach 1
    # 
    # Runtime complexity - O(nlog(n))
    #
    # Space complexity - O(1) -> since we are sorting in-place
    #
    # nums.sort()
    # for i in range(1, len(nums)):
    #     if nums[i] == nums[i - 1]:
    #         return nums[i]
    
    #
    # Approach 2 (same concept as https://leetcode.com/problems/linked-list-cycle-ii/)
    #
    # Runtime complexity - O(n)
    #
    # Space complexity - O(1)
    #
    # only applicable when range of numbers are within indices [1, n]
    #
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        # "entrance" to cycle found
        if slow == fast:
            
            # start slow again from beginning to eventually meet
            slow = nums[0]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow

nums = [1, 3, 4, 2, 2]
nums = [3, 1, 3, 4, 2]

print(findDuplicate(nums))
