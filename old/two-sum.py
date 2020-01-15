# Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            search_elem = target - nums[i]
            j = i + 1
            while j < len(nums):
                if search_elem == nums[j]:
                    return (i, j)
                j += 1