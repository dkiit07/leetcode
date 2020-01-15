# Subtract the Product and Sum of Digits of an Integer
# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """

        num_arry = []
        while n is not 0:
            num = n % 10
            n = n/ 10
            num_arry.append(num)

        sum = 0
        prod = 1
        for i in num_arry:
            sum += i
            prod *= i

        return prod - sum
