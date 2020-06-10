import heapq
from collections import defaultdict


#  Uses simple BFS - Accepted
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, queue = [0] + [float("inf")] * N, defaultdict(list), deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while queue:
            time, node = queue.popleft()
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    queue.append((time + w, v))
        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1


# (u,v,w) 通过每次弹出现有邻居中的最小值来更新当前结点的值来保证最小，相当于所有的边都遍历过一遍了
class Solution:
    def networkDelayTime(self, times, N, K):
        elapsedTime, graph, heap = [0] + [float("inf")] * N, defaultdict(list), [(0, K)]
        for u, v, w in times:
            graph[u].append((v, w))

        while heap:
            time, node = heapq.heappop(heap, )
            print(time, node, elapsedTime[node])
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:  # 添加邻居
                    heapq.heappush(heap, (time + w, v))
                print(heap, elapsedTime[node])

        mx = max(elapsedTime)
        return mx if mx < float("inf") else -1

# Dijistra： 找到当前最小的，更新邻居，如果不是最小，说明和之前的结果重复了，因此不需要继续操作
class Solution:
    def networkDelayTime(self, times, N, K):
        arrive_time = [0] + [float('inf')] * N
        cur_neighbors = [(0, K)]
        neighbors = defaultdict(list)
        for time in times:
            neighbors[time[0]].append(time[1:])
        # print(neighbors)

        while cur_neighbors:
            time, node = heapq.heappop(cur_neighbors)
            # print(time, node)
            if arrive_time[node] > time:        # 只有更新的结点才在这个基础上更新邻居
                arrive_time[node] = time
                for neighbor in neighbors[node]:
                    heapq.heappush(cur_neighbors, (neighbor[1] + time, neighbor[0]))
                # print(cur_neighbors, arrive_time[node])

        res = max(arrive_time)
        return res if res < float('inf') else -1


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2
    res = sol.networkDelayTime(data[0], data[1], data[2])
    print(res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 3)
                nums.append(num1)
            print('the nums are', nums)
            res = sol.hasGroupsSizeX(data)
            print(res)


test(Solution, False)
