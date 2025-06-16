#https://www.geeksforgeeks.org/problems/find-the-frequency/1

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        frequency = 0
        for num in arr:
            if num == x:
                frequency += 1
                
        return frequency
