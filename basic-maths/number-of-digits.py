from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   # Write your code here.
   count = 0
   while n > 0:
      n //= 10
      count += 1
   return count
   '''
   if n == 0:
      return 1
   return int(log(abs(n),10) + 1)
   '''
