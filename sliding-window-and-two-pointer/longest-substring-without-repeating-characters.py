# https://leetcode.com/problems/longest-substring-without-repeating-characters
# O(n), O(n), using sliding window & two pointer
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maximum = 0
        l, r = 0, 0
        my_dict = {}
        while r < n:
            if s[r] in my_dict:
                l = max(l,my_dict[s[r]]+1)
            maximum = max(maximum, r-l+1)
            my_dict[s[r]] = r
            r += 1

        return maximum
        
# O(n^2), O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maximum = 0
        for i in range(n):
            my_set = set()
            for j in range(i,n):
                if s[j] in my_set:
                    break
                maximum = max(maximum,j-i+1)
                my_set.add(s[j])

        return maximum
