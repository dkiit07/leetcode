# Flipping an Image
# https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for row in A:
            if(len(row ) %2 == 0):
                size = int(len(row ) /2)
            else:
                size = int(len(row ) /2) + 1

            for i in range(size):
                temp = row[i]

                row[i] = row[len(row ) - 1 -i]
                i f(row[i] == 0):
                    row[i] = 1
                else:
                    row[i] = 0
                row[len(row ) - 1 -i] = temp
                i f(row[len(row ) - 1 -i] == 0):
                    row[len(row ) - 1 -i] = 1
                else:
                    row[len(row ) - 1 -i] = 0

        return A
