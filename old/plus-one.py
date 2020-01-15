# Plus One
# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)

        while digits[n - 1] == 9:
            digits[n - 1] = 0
            n -= 1
        if n == 0:
            digits = [1] + digits
        else:
            digits[n - 1] += 1

        return digits