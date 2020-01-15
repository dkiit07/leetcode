# Decompress Run-Length Encoded List
# https://leetcode.com/problems/decompress-run-length-encoded-list/


class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        new_nums = []
        for i in range(len(nums)):
            if i % 2 == 0:
                for j in range(nums[i]):
                    new_nums.append(nums[i + 1])
        return new_nums
