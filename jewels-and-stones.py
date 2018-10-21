# Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for jewel in range(len(J)):
            for stone in range(len(S)):
                if J[jewel] == S[stone]:
                    count += 1
        return count