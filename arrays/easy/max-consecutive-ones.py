# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        count_max = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count_max = max(count, count_max)
                count = 0

        return max(count_max,count) #in case if list ended on 1, loop will not go in else

"""
Time: O(n) — single pass

Space: O(1) — only counters used

So this is already as optimal as it gets.
"""
