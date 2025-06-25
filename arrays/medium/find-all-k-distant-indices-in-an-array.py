# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        last_added = 0
        result = []
        
        for j in range(n):
            if nums[j] == key:
                start = max(last_added,j-k)
                end = min(n-1,j+k)
                for i in range(start, end+1):
                    result.append(i)
                last_added = end + 1 # move pointer to avoid re-adding
        
        return result

"""
Time: O(n)
Space: O(n) — for result list in worst case
"""

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_idx = [i for i, val in enumerate(nums) if val == key]
        result = []
        for i in range(n):
            for j in key_idx:
                if abs(i-j) <= k:
                    result.append(i)
                    break

        return result

"""
Time: O(n2)
Space: O(n)
"""
