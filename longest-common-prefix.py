# Longest common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        str_arr = []
        shortest_word_len = 10000
        for word in strs:
            if word == "":
                return ""
            else:
                word_list = list(word)
                if len(word_list) < shortest_word_len:
                    shortest_word_len = len(word_list)
                str_arr.append(word_list)
        print(str_arr)
        common_predix = ""
        i = -1
        break_flag = False
        for i in range(shortest_word_len):
            common_predix = str_arr[0][i]
            for word in str_arr:
                if common_predix != word[i]:
                    break_flag = True
                else:
                    pass
            if break_flag == True:
                break
        if i > 0 and break_flag == True:
            return strs[0][:i]
        elif i > 0 and break_flag == False:
            return strs[0][:i + 1]
        if i == 0 and break_flag == False:
            return strs[0][0]
        else:
            return ""