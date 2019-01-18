# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s_new = s.lower()
        s_arr = []
        for i in range(len(s_new)):
            if s_new[i].isalpha() or s_new[i].isalnum():
                s_arr.append(s_new[i])
            else:
                pass
        j = 0
        k = len(s_arr) - 1
        while (j != k and j < k):
            if s_arr[j] == s_arr[k]:
                j += 1
                k -= 1
            else:
                return False

        return True