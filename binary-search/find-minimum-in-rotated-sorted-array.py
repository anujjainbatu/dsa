# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minimum = float("inf")

        while r >= l:
            mid = (r+l)//2
                
            if nums[mid] >= nums[l]: 
                '''left part is sorted, minimum will be either 
                smallest of this part or exist in unsorted part'''
                minimum = min(minimum,nums[l])
                l = mid+1
            else:
                #right part is sorted, minimum will exist in unsorted part
                minimum = min(minimum,nums[mid])
                r = mid - 1

        return minimum
