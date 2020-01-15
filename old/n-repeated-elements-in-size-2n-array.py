# N-Repeated Element in Size 2N Array
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        if A[0] == A[1] or A[0] == A[-1]:
            return A[0]
        if A[-1] == A[-2]:
            return A[-1]

        prev = A[0]
        for i in range(len(A) - 2):
            if A[i] == A[i + 1]:
                return A[i]
            elif prev + A[i + 1] - A[i + 2] == A[i + 1]:
                return prev
            prev = A[i + 1]
