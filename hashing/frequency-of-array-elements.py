# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr):
        #  code here
        n = len(arr)
        frequency = [0 for x in range(n)]
        
        for x in arr:
            index = x-1
            frequency[x-1] += 1
            
        return frequency

