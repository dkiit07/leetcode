# Reverse String
# https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_str = ''
        for char in range(len(s)):
            rev_str = rev_str + s[len(s) - char - 1]
        return rev_str