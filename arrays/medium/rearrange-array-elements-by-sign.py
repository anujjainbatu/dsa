# https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive_list = []
        negative_list = []
        for num in nums:
            if num < 0:
                negative_list.append(num)
            else:
                positive_list.append(num)

        result = []

        for i in range(n//2):
            result.append(positive_list[i])
            result.append(negative_list[i])

        return result

"""
Time: O(n + n/2)
Space: O(n)
"""

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        p, n = 0, 1

        for num in nums:
            if num < 0:
                result[n] = num
                n += 2
            else:
                result[p] = num
                p += 2

        return result

"""
Time: O(n)
Space: O(n)
"""
