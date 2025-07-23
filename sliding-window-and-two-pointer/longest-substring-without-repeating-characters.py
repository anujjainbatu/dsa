# https://leetcode.com/problems/longest-substring-without-repeating-characters
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
