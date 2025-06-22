#https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1

class Solution:
    #Complete the below function
    def search(self,arr, x):
        n = len(arr)
        for i in range(n):
            if arr[i] == x:
                return i
                
        return -1
