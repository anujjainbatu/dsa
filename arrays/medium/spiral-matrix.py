# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while bottom >= top and right >= left:
            # left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # right to left
            if bottom >= top:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # bottom to top
            if right >= left:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
