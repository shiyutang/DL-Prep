# -*- coding:utf-8 -*-
import heapq


class Solution:
    def __init__(self):
        self.large, self.small = [], []

    def Insert(self, num):
        if len(self.large) == len(self.small):
            heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        # print(self.large, self.small)

    def GetMedian(self):
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])


# 5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00


sol = Solution()
sol.Insert(5)
print(sol.GetMedian())
sol.Insert(2)
print(sol.GetMedian())
sol.Insert(3)
print(sol.GetMedian())
sol.Insert(4)
print(sol.GetMedian())
sol.Insert(1)
print(sol.GetMedian())
sol.Insert(6)
print(sol.GetMedian())
sol.Insert(7)
print(sol.GetMedian())
sol.Insert(0)
print(sol.GetMedian())
sol.Insert(8)
print(sol.GetMedian())
