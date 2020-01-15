# Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        for elem in nums:
            count = 0
            while elem is not 0:
                num = elem % 10
                elem = elem / 10
                count += 1
            if count % 2 is 0:
                res += 1
        return res
