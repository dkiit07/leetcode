# Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/


class Solution:
    def defangIPaddr(self, address: str) -> str:
        returned_add = "";
        for char in address:
            if char == '.':
                returned_add = returned_add + '[.]'
            else:
                returned_add = returned_add + char
        return returned_add

