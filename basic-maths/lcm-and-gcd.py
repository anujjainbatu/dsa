class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        num1, num2 = a, b
        while num2 > 0:
            num1, num2 = num2, num1%num2
            
        #num1 = gcd
        
        lcm = abs(a*b)//num1
        
        return [lcm, num1]
            
