# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        lower = self.lower_bound(arr, target)
        if lower == len(arr) or arr[lower] != target:
            return 0
            
        upper = self.upper_bound(arr, target)
        return upper - lower
    
    def lower_bound(self, arr, target):
        l, r = 0, len(arr)
        
        while l < r:
            mid = (l+r)//2
            
            if arr[mid] < target:
                l = mid + 1
            else:
                r = mid
                
        return l
        
    def upper_bound(self, arr, target):
        l, r = 0, len(arr)
        
        while l < r:
            mid = (l+r)//2
            
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid
                
        return l
        
    
