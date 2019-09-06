# Peak Index in a Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        max_val = A[0]
        idx = 0
        max_idx = 0
        for elem in A:
            if elem >= max_val:
                max_val = elem
                max_idx = idx
            idx += 1
        return max_idx
