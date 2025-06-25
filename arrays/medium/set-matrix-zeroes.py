# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        zero_idx_i = set()
        zero_idx_j = set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_idx_i.add(i)
                    zero_idx_j.add(j)
                

        for i in zero_idx_i:
            for j in range(m):
                matrix[i][j] = 0

        for j in zero_idx_j:
            for i in range(n):
                matrix[i][j] = 0

# O(n*m)
