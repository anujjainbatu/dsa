# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        l = 0
        r = len(arr) - 1
        floor = -1
        
        while r >= l:
            mid = (r+l)//2
            if arr[mid] <= x:
                l = mid+1
                floor = mid
            else:
                r = mid-1
                
        return floor
