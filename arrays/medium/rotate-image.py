#https://leetcode.com/problems/rotate-image/

#fastest but violates questions in-place requirement guidelines
import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        temp = copy.deepcopy(matrix)

        for i in range(n):
            for j in range(m):
                matrix[j][n-1-i] = temp[i][j]
