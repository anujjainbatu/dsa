# https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                k, l = j + 1, n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]

                    if total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return result

"""
Time Complexity: O(n^3)
Space Complexity: O(1) (excluding output)
"""

class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        result.add(quad)
                    seen.add(nums[k])

        return [list(q) for q in result]

"""
Time Complexity: O(n^3)
Space Complexity: O(n) (for hash sets)
"""
