# Length of Last Word
#  https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s.strip()
        str_list = str.split(' ')
        if len(str_list) == 1 and str_list[0] == ' ':
            return 0
        else:
            return len(str_list[-1])