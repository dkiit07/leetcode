# Remove Element
# https://leetcode.com/problems/remove-element/


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        val_index = []
        for i in range(len(nums)):
            if nums[i] == val:
                val_index.append(i)
                # nums[i] = -1

        len_value = len(val_index)
        if len_value == 0:
            return len(nums)

        for j, num in reversed(list(enumerate(nums))):
            if nums[j] != val and len(val_index) != 0:
                nums[min(val_index)] = nums[j]
                val_index.remove(min(val_index))

        return len(nums) - len_value