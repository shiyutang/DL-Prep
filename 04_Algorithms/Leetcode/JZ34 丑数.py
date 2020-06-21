# -*- coding:utf-8 -*-
# 每次在现有丑数的基础上，乘以2，3，5，找到最小的丑数
class Solution:
    def GetUglyNumber_Solution(self, index):
        Uglys = [1]
        p1, p2, p3 = 0, 0, 0  # 每次记录上一个乘以 x 的位置，乘了其他数的不着急乘，先乘没乘过的
        if index < 0:
            return
        elif index == 0:
            return 0
        else:
            while len(Uglys) < index:
                minres = min(Uglys[p1] * 2, min(Uglys[p2] * 3, Uglys[p3] * 5))
                if Uglys[p1] * 2 == minres:
                    p1 += 1
                if Uglys[p2] * 3 == minres:
                    p2 += 1
                if Uglys[p3] * 5 == minres:
                    p3 += 1
                Uglys.append(minres)
        return Uglys[-1]


sol = Solution()
print(sol.GetUglyNumber_Solution(15))
