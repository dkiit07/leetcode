# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        counter = 1
        i = 1
        for ii in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                temp = nums[i]
                nums.pop(i)
                nums.append(temp)
                i -= 1
            else:
                counter += 1
            i += 1
        return counter
