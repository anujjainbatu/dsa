# https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1

class Solution:
    def checkKthBit(self, n, k):
        if (n & (1<<k)) == 0:
            return False
        else:
            return True
