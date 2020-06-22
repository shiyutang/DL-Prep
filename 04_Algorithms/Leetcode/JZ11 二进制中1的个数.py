# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        cnt = 0
        mark = 0x01
        for _ in range(32):
            if mark & n:
                cnt += 1
            mark <<= 1
        return cnt

# method2: val 每次和自己的减一相与就会少一个1，一直到val为0 即可


sol = Solution()
print(sol.NumberOf1(-1))