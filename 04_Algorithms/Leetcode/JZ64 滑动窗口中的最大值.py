
# 可以用单调栈，找到邻近更大的，如果有效则加入比较，如果没有，则自己为最大，这样为 O（n）
# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        res = []
        if size == 0:
            return res
        for idx in range(len(num) - size + 1):
            sample = num[idx:idx + size]
            res.append(max(sample))
        return res


sol = Solution()
res = sol.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3)
print(res)
