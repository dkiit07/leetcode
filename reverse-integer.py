# Reverse Integer
# https://leetcode.com/submissions/detail/186955046/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        x_str = str(x)
        minus = False
        if x_str[0] == '-':
            minus = True
            x_str = x_str[1:]
        rev_str = x_str[::-1]
        rev_x = int(rev_str)
        if minus == True:
            rev_x = 0 - rev_x
        if rev_x >= (2 ** 31) - 1 or rev_x < -2 ** 31:
            return 0
        else:
            return rev_x
