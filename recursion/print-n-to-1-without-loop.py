# https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1

class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=" ")
        self.printNos(n-1)
