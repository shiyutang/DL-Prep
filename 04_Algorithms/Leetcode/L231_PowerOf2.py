import math

class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        k = math.log(n,2)
        if k%1 - 0 > 0.00000000000001:
            return False
        else:
            return True