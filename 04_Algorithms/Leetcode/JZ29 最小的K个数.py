# -*- coding:utf-8 -*-
import bisect


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k == 0:   # 变量的长度范围要考虑清楚
            return []
        package = tinput[:k]
        package.sort()
        for i in range(k, len(tinput)):
            if tinput[i] < package[-1]:
                idx = bisect.bisect_left(package, tinput[i])
                package.insert(idx, tinput[i])
                package = package[:k]
        return package


sol = Solution()
print(sol.GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))

