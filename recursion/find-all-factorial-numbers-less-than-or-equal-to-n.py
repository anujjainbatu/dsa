# https://www.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0

class Solution:
    def factorialNumbers(self, n):
        list = []
    	for i in range(1, n+1):
    	    number = self.factorial(i)
    	    if number <= n:
    	        list.append(number)
    	    else:
    	        break
    	        
    	return list
    	    
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n-1)
