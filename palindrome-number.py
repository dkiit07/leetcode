# Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)
        n = len(x_str)
        is_palin = True
        i=0
        while i <= n/2:
            if x_str[i] != x_str[n-1-i]:
                is_palin = False
            i += 1
        return is_palin