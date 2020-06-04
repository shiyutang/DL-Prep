import heapq

class Solution:
    def scheduleCourse(self, A):
        pq = []   # priority queue
        start = 0
        for t, end in sorted(A, key = lambda x:x[1]):
            start += t
            heapq.heappush(pq, -t)
            print(pq)
            while start > end:
                start += heapq.heappop(pq)
                print(pq)
        return len(pq)

sol = Solution()
sol.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])