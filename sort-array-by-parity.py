# Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        even_list = []
        odd_list = []

        for elem in A:
            if elem % 2 == 0:
                even_list.append(elem)
            else:
                odd_list.append(elem)
        return even_list + odd_list
