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

'''
Time complexity: 
O(n^2)

Space complexity: 
O(n^2)
'''

#in-place
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) #n = m

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
                #only upper triangle value goes in loop to prevent reswapping

        
        for row in matrix:
            l = 0
            r = n-1
            while r > l:
                row[r], row[l] = row[l], row[r]
                l += 1
                r -= 1

'''
Time complexity: 
O(n^2)

Space complexity: 
O(1)
'''
        

            

