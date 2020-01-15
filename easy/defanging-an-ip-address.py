# Defanging an IP Address
# https://leetcode.com/problems/defanging-an-ip-address/


class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        new_add = ''

        for ch in address:
            if ch == '.':
                ch = '[.]'
            new_add += ch
        return new_add
