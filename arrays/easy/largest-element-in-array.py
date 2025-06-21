# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0

class Solution:
    def largest(self, arr):
        largest = float("-inf")
        for nums in arr:
            if nums > largest:
                largest = nums
                
        return largest
