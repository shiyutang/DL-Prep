class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        mark = [False for i in range(intervals[-1].end)]
        # give color based on intervals
        for interval in intervals:
            i = interval.start
            while i+1 in range(interval.start,interval.end+1):
                mark[i] = True
                i += 1
        print(mark)
        # color use new interval
        k = newInterval.start
        while k+1 in range(newInterval.start,newInterval.end+1):
            mark[k] = True
            k += 1
        print(mark)
        # collect color
        newintervals = []
        interval = Interval()
        for j in range(len(mark)):
            if mark[j] == True and interval.start == 0:
                interval.start = j
            if (mark[j] == False and j>= 1 and mark[j-1] == True) :
                interval.end = j
                print(interval.start)
                print(interval.end)
                newintervals.append(interval)
                interval = Interval()
            elif j == len(mark)-1 and mark[j]==True:
                interval.end = j+1
                print(interval.start)
                print(interval.end)
                newintervals.append(interval)
                interval = Interval()
        return newintervals

sol = Solution()
interval1 = Interval(1,3)
interval2 = Interval(6,9)
intervals = [interval1,interval2]
interval3 = Interval(2,5)
sol.insert(intervals,interval3)