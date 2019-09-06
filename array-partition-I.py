# Array Partition I
# https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        min_sum = 0
        for i in range(int(len(sorted_nums) / 2)):
            min_sum += min(sorted_nums[2 * i], sorted_nums[(2 * i) + 1])
        return min_sum
