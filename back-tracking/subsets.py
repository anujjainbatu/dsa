# https://leetcode.com/problems/subsets/
# O(2^n), O(n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        self.generate_subsets(0, [], nums, power_set)
        return power_set

    def generate_subsets(self, idx, subset, nums, power_set):
        if idx >= len(nums):
            power_set.append(subset.copy())
            return
        # Include nums[idx]
        subset.append(nums[idx])
        self.generate_subsets(idx+1, subset, nums, power_set)
        # Exclude nums[idx]
        subset.pop()
        self.generate_subsets(idx+1, subset, nums, power_set)

  
