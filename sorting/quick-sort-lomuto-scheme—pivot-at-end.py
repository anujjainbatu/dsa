# https://www.geeksforgeeks.org/problems/quick-sort/1

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            p_index = self.partition(arr, low, high)
            self.quickSort(arr, low, p_index - 1)
            self.quickSort(arr, p_index + 1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low,high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        
        return i+1
    
