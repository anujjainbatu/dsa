# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# My code 1:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set(nums)
        n = len(nums)
        k = 0
        for num in nums:
            if num in unique_set:
                nums[k] = num
                unique_set.remove(num)
                k += 1
        return k


# My code 2:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 1
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k
