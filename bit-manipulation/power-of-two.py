# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        16 = 1000 & 15 = 0111
        '''
        if n > 0 and n & n-1 == 0:
            return True
        else:
            return False
        
