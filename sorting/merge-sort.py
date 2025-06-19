# https://www.geeksforgeeks.org/problems/merge-sort/1
# in-place: chaning org array
class Solution:
 
    def mergeSort(self,arr, l, r):
        if l >= r:
            return arr[l:r+1]
        mid = (l+r)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        self.merge(arr, l, mid, r)
        
    def merge(self, arr, l, mid, r):
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]
        i = j = 0
        n, m = len(left), len(right)
        k = l
        while i < n and j < m:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
                
        while i < n:
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < m:
            arr[k] = right[j]
            j += 1
            k += 1

#Making new array
class Solution:
 
    def mergeSort(self,arr, l, r):
        if l >= r:
            return arr[l:r+1]
        mid = (l+r)//2
        left = self.mergeSort(arr, l, mid)
        right = self.mergeSort(arr, mid+1, r)
        return self.merge(left, right)
        
    def merge(self, arr1, arr2):
        i, j = 0, 0
        n, m = len(arr1), len(arr2)
        result = []
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
                
        if i < n:
            result.extend(arr1[i:])
            
        if j < m:
            result.extend(arr2[j:])
            
        return result
