#https://www.geeksforgeeks.org/problems/palindrome-string0817/1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
		return self.recIsPalindrome(s, l, r)
		
	def recIsPalindrome(self, s: str, l: int, r: int) -> bool:
	    if l > r:
	        return True
	    if s[l] != s[r]:
	        return False
	    return self.recIsPalindrome(s, l+1, r-1)
