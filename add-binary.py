# Add Binary
# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_num = int(a)
        b_num = int(b)
        c_num = a_num + b_num
        c = "0" + str(c_num)
        n = len(c)
        c_list = list(c)

        while n > 0:
            if int(c_list[n - 1]) == 2:
                c_list[n - 1] = str(0)
                c_list[n - 2] = str(int(c_list[n - 2]) + 1)
            if int(c_list[n - 1]) == 3:
                c_list[n - 1] = str(1)
                c_list[n - 2] = str(int(c_list[n - 2]) + 1)
            n -= 1
        if c_list[0] == "0":
            c_list = c_list[1:]
        return ''.join(c_list)