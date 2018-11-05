# Valid Parentheses
# https://leetcode.com/submissions/detail/187592200/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s = list(s)
        test_list = []
        if len(s) == 1 or len(s)%2 == 1:
            return False
        else:
            if s[0] == ')' or s[0] == '}' or s[0] == ']':
                return False
            for i in range(len(s)):
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    test_list.append(s[i])
                elif s[i] == ')' and test_list[-1] == '(':
                    test_list.pop()
                elif s[i] == '}' and test_list[-1] == '{':
                    test_list.pop()
                elif s[i] == ']' and test_list[-1] == '[':
                    test_list.pop()
                else:
                    return False
            if len(test_list) == 0:
                return True
            return False