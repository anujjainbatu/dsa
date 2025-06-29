# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        lower_bound = n

        while r >= l:
            mid = (l+r)//2

            if target <= nums[mid]:
                lower_bound = mid
                r = mid-1
            else:
                l = mid+1

        return lower_bound
