# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx,val in enumerate(nums):
            diff = target - val
            if diff in hash_map:
                return idx, hash_map[diff]
            else:
                hash_map[val] = idx
'''
Time complexity: O(n)
Space complexity: O(n)
'''
