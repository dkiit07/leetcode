# Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        num_list = []
        is_self = True
        for num in range(left, right + 1):
            if self.oneNumber(num):
                num_list.append(num)
        return num_list

    def oneNumber(self, num: int) -> int:
        ret = True
        for n in str(num):
            if int(n) != 0:
                if num % int(n) != 0:
                    ret = False
            else:
                ret = False
        return ret

