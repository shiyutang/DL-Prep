class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []
        self.cnt = 0

    def addNum(self, num: int) -> None:
        if self.cnt is 0:
            self.val = [num]
        else:
            for i in range(self.cnt):
                if num < self.val[i]:
                    break

            if i < self.cnt - 1:
                self.val.insert(i, num)
            else:
                self.val.insert(i + 1, num)
        self.cnt += 1
        print(self.val)

    def findMedian(self) -> float:
        middle = self.cnt // 2
        if self.cnt % 2 == 0:
            return (self.val[middle] + self.val[middle - 1]) / 2
        else:
            return self.val[middle]
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# ["MedianFinder","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]
# [[],[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]