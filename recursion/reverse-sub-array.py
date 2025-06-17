#https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1

class Solution:
	def reverseSubArray(self,arr,l,r):
		if l >= r:
		    return arr
		temp = arr[l-1]
		arr[l-1] = arr[r-1]
		arr[r-1] = temp
		l += 1
		r -= 1
		return self.reverseSubArray(arr,l,r)
