# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        for char in t:
            if char in hash_map:
                hash_map[char] -= 1
            else:
                return False

            if hash_map[char] < 0:
                return False
        
        for value in hash_map.values():
            if value != 0:
                return False

        return True

'''
Time: O(n)
Space: O(1) can go max to 26 char
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

        '''
        Counter(s) creates a frequency dictionary for string s
        Same for t
        Then it just compares the two dictionaries
        '''

'''
Time: O(n)
Space: O(1)
'''
