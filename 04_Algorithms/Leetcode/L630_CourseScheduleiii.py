# 选课问题，对于截止时间由先到后，如果前k个课程时间超出了最后一个截止时间，把时间最长的课程排除

import heapq

class Solution:
    def scheduleCourse(self, courses):
        start = 0
        heap = []
        courses.sort(key = lambda x:x[1])
        
        for length, end in courses:
            start += length
            heapq.heappush(heap,-length)
            print(heap)
            if start > end:
                print("need delete",heap)
                start = start + heapq.heappop(heap)  #优先值最小的先pop出
        print(len(heap))
        return len(heap)

sol = Solution()
sol.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
sol.scheduleCourse([[5,5],[4,6],[2,6]])