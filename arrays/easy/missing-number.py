# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        complete_sum = n*(n+1)//2
        return complete_sum - sum(nums)

"""
Time complexity: O(n)
We traverse the list once to compute the sum.

Space complexity: O(1)
No extra data structures are used; just variables.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dict = {}
        for i in range(n+1):
            dict[i] = 0
        for x in nums:
            dict[x] += 1
        
        for key,val in dict.items():
            if val == 0:
                return key

        return 0
