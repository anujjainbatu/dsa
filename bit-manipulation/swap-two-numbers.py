# https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1

class Solution:
    def get(self, a: int, b: int) -> tuple[int, int]:
        # code here
        a = a^b
        b = a^b #(a^b)^b => b
        a = a^b #(a^b)^b => (a^b)^a 
        
        return (a, b)
