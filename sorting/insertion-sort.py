# https://www.geeksforgeeks.org/problems/insertion-sort/0
class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = key
                
        return arr
