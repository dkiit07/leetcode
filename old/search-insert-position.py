# Search Insert Position
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0
        if nums[0] > target:
            return 0
        if nums[len(nums) - 1] < target:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif i < len(nums) - 1:
                if nums[i] < target and nums[i + 1] > target:
                    return i + 1