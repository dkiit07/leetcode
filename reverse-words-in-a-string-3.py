# Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_array = []
        str_array = s.split()
        for word in str_array:
            word = word[::-1]
            rev_array.append(word)
        return ' '.join(rev_array)