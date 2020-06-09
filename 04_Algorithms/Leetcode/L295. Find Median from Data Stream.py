# didn't pass the last one, too slow
from heapq import *


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.big) == len(self.small):
            heappush(self.big, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.big, num))

    def findMedian(self) -> float:
        if len(self.big) == len(self.small):
            return (self.big[0] - self.small[0]) / 2
        else:
            return self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

from heapq import *


# 堆排序的特点：每次插入一个结点只需要 lg(h),h 为排序的层高，因为非常适合对差不多排序好的序列进行快速排序

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # O(3lgN), find_medium O(1)
        self.large = []  # min heap
        self.small = []  # max heap

    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            heappush(self.large, -heappushpop(self.small, -num))  # 将-num 加入到max heap，并返回最小的数，每次会先向 self.large中加入较大的数
        else:
            heappush(self.small, -heappushpop(self.large, num))  # 然后把large中较小的数放到small中
        print(self.small, self.large)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0  # small中最大和large中最小
        else:
            return float(self.large[0])
