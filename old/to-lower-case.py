# To Lower Case
# https://leetcode.com/problems/to-lower-case/

class Solution:
    def toLowerCase(self, str: str) -> str:
        new_str = ""
        for char in str:
            if ord(char) >= 65 and ord(char) <= 90:
                new_str = new_str + chr(ord(char)+32)
            else:
                new_str = new_str + char
        return new_str
