# https://leetcode.com/problems/rotate-array/description/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums) #in case k > n
        
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
    """   
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    """
# Time Complexity: O(n), Space Complexity: O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < k:
            k = k%n
        
        nums[:] = nums[n-k:] + nums[0:n-k]
        # nums[:] ensures change is inplace
        return nums
# Time Complexity: O(n), Space Complexity: O(n)
