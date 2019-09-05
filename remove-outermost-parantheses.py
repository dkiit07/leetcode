# Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        flag = 0
        p_str = ""
        p_str_list = []
        for ch in S:
            if ch == '(':
                flag += 1
                p_str += str(ch)
            else:
                flag -= 1
                p_str += str(ch)
            if flag == 0:
                p_str_list.append(p_str)
                p_str = ""
        p_str_list = [str[1:-1] for str in p_str_list]
        str_join = "".join(p_str_list)
        return str_join
