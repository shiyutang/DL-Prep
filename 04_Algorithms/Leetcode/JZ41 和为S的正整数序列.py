# -*- coding:utf-8 -*-
from math import ceil

# 
class Solution:
    def FindContinuousSequence(self, tsum):
        # 奇数个是tsum整除个数，偶数个是tsum除得有x.5
        res = []
        for i in range(2, tsum):
            if (i % 2 == 0 and tsum % i == 0.5 * i) or (i % 2 == 1 and tsum % i == 0):
                start = ceil(tsum / i) - i // 2
                if start > 0:
                    res.append([start + i for i in range(i)])

        res.sort(key=lambda s: s[0])
        return res


sol = Solution()
print(sol.FindContinuousSequence(3))
