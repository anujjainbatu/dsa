# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        f_o = l_o = -1

        for i in range(n):
            if nums[i] == target:
                if f_o == -1:
                    f_o = i
                l_o = i

        return f_o, l_o

  # was required in (log(n))

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        first = self.lower_bound(nums, target)
        if first == n or nums[first] != target:
            return [-1, -1]  # Target not found

        last = self.upper_bound(nums, target) - 1
        return [first, last]

    def lower_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def upper_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
