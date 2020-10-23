# 每次要选择质量之和最小的人， 但是前面的最优组合不一定是质量最小的，只是选择不同的ratio下最好，应当找到给定情况下质量之和最小，并在每次等于k的时候，算得结果累计最小值
class Solution1:
    def mincostToHireWorkers(self, quality, wage, K: int):
        from fractions import Fraction
        workers = sorted(((Fraction(w, q), q, w) for q, w in zip(quality, wage)))
        print(workers)

        costmemoi = [[(float('inf'), float('inf')) for _ in range(K + 1)] for _ in range(len(quality))]
        # save the most
        for i in range(len(quality)):
            costmemoi[i][0] = (0, 0)

        for idx in range(len(quality)):
            for nbrPeople in range(1, min(K + 1, idx + 2)):
                previouscost, currentcost = costmemoi[idx - 1][nbrPeople], costmemoi[idx - 1][nbrPeople - 1]

                if previouscost[0] * previouscost[1] < (currentcost[1] + workers[idx][1]) * workers[idx][0]:
                    costmemoi[idx][nbrPeople] = previouscost
                    print('the cost in idx {} is {} with {} people'.format(idx, previouscost, nbrPeople))

                elif previouscost[0] * previouscost[1] == (currentcost[1] + workers[idx][1]) * workers[idx][0]:
                    if previouscost[1] < workers[idx][1]:
                        costmemoi[idx][nbrPeople] = previouscost
                        print('the cost in idx {} is {} with {} people'.format(idx, previouscost, nbrPeople))

                    else:
                        costmemoi[idx][nbrPeople] = (workers[idx][0], currentcost[1] + workers[idx][1])
                        print(
                            'the cost in idx {} is {} with {} people'.format(idx, costmemoi[idx][nbrPeople], nbrPeople))
                else:
                    costmemoi[idx][nbrPeople] = (workers[idx][0], currentcost[1] + workers[idx][1])
                    print('the cost in idx {} is {} with {} people'.format(idx, costmemoi[idx][nbrPeople], nbrPeople))

        return costmemoi[len(quality) - 1][K][0] * costmemoi[len(quality) - 1][K][1]

import heapq

# 找到当前ratio 小前面求和最小的工人
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        from fractions import Fraction
        workers = sorted((Fraction(w, q), q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)   # 维护质量最小
            sumq += q                  # 小于K则一直相加

            if len(pool) > K:
                sumq += heapq.heappop(pool)  # 把求和结果去除较大的值

            if len(pool) == K:
                ans = min(ans, ratio * sumq)  # 结果等于最小的那个

        return float(ans)


sol = Solution()
# print(sol.mincostToHireWorkers(quality=[10, 20, 5], wage=[70, 50, 30], K=2))
# print(sol.mincostToHireWorkers(quality=[3, 1, 10, 10, 1], wage=[4, 8, 2, 2, 7], K=3))
print(sol.mincostToHireWorkers(quality=[2, 1, 5], wage=[17, 6, 4], K=2))
