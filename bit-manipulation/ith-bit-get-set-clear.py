# https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1

class Solution:
    def bitManipulation(self, num, i):
        ith_bin = self.get_bit(num, i)
        set_ith_bin = self.set_bit(num, i)
        clear_ith_bin = self.clear_bit(num, i)
        
        print(ith_bin, set_ith_bin, clear_ith_bin, sep = " ")
        
    # opeartion performed on i-1 becuase question gave 1 based indexing
        
    def get_bit(self, num, i):
        if (num & (1 << i-1)): #by right shift (num>>i-1) & 1
            return 1
        else:
            return 0
            
    def set_bit(self, num, i):
        return num | (1 << i-1)
        
    def clear_bit(self, num, i):
        return num & ~(1 << i-1)
        
