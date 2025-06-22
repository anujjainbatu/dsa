# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        nums[k:] = [0]*(n-k)

'''
Time complexity: O(n)
(We iterate through the array once and assign values directly.)

Space complexity: O(1)
(We use only a few variables — no additional data structures.)
'''
        
