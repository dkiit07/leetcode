# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        while m + n >= 0 and m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                m -= 1
                nums1[m + n] = nums1[m]
                nums1[m] = 0
            if nums1[m - 1] <= nums2[n - 1] and n > 0:
                n -= 1
                nums1[m + n] = nums2[n]
        while n > 0:
            n -= 1
            nums1[n] = nums2[n]

