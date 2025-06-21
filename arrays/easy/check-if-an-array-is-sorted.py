# https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        n = len(arr)
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                return False
                
        return True
