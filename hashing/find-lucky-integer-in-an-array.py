# https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_map = {}
        lucky_int = -1

        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1

        for key, val in hash_map.items():
            if key == val:
                lucky_int = max(lucky_int, key)

        return lucky_int

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
