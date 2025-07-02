# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while r >= l:
            mid = (r+l)//2

            if nums[mid] == target:
                return True
            # Left half is sorted
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
                
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

"""
Average Case: O(log N) as the search space is generally halved.
Worst Case: Can degrade to O(N). This happens when there are many duplicate elements, especially if nums[low] == nums[mid] == nums[high] repeatedly, such as . In this scenario, low++ and high-- only reduce the search space by two elements at a time, rather than halving it, leading to a linear scan-like behavior
"""


