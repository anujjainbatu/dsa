# https://www.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i,n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[min_idx], arr[i] = arr[i], arr[min_idx]
            
        return arr
