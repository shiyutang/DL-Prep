class Solution:
    def minCost(self, houses: list, cost, m: int, n: int, target: int):
        costmemoi = [[[float('inf') for _ in range(m)] for __ in range(n)] for ___ in range(m)]
        # find min(costmemoi[len(houses)-1][j][target])
        blocks = 0
        if houses[0] == 0:
            for j in range(n):
                costmemoi[0][j][blocks] = cost[0][j]
                # print("house {} paint color {} with accumulative cost {} and total block is {}".format(0, j, cost[0][j],
                #                                                                                        blocks + 1))
        else:
            costmemoi[0][houses[0] - 1][blocks] = 0
            # print("house {} have color {} with accumulative cost {} and total block is {} ".format(0, houses[0] - 1, 0,
            #                                                                                       blocks + 1))

        for i in range(1, m):
            for blocks in range(i):  # i-1座房子有至多i-1个block
                for j in range(n):  # 之前的n种颜色
                    if houses[i] == 0:
                        for jj in range(n):  # n种颜色，每个颜色都尝试涂色
                            # print(i, blocks, j, jj, m, m, n, n)
                            if jj == j:
                                costmemoi[i][jj][blocks] = min(costmemoi[i - 1][j][blocks] + cost[i][jj],
                                                               costmemoi[i][jj][blocks])
                                # print("house {} paint color {} with accumulative cost {} and total block is {
                                # }".format(i, jj, costmemoi[i][jj][blocks], blocks + 1))
                            else:
                                costmemoi[i][jj][blocks + 1] = min(costmemoi[i - 1][j][blocks] + cost[i][jj],
                                                                   costmemoi[i][jj][blocks + 1])
                                # print("house {} paint color {} with accumulative cost {} and total block is {}".format(i, jj, costmemoi[i][jj][blocks + 1],
                                #                                                                                       blocks + 2))
                    else:
                        # print(i, blocks, j, m, m, n)
                        if j == (houses[i] - 1):
                            costmemoi[i][houses[i] - 1][blocks] = min(costmemoi[i][houses[i] - 1][blocks],
                                                                      costmemoi[i - 1][j][blocks])
                            # print("house {} have color {} with accumulative cost {} and total block is {} when previous color is {}".format(i, houses[i] - 1, costmemoi[i - 1][j][blocks],
                            #                                                                       blocks + 1, j))
                        else:
                            costmemoi[i][houses[i] - 1][blocks + 1] = min(costmemoi[i][houses[i] - 1][blocks + 1],
                                                                          costmemoi[i - 1][j][blocks])
                            # print("house {} have color {} with accumulative cost {} and total block is {} when previous color is {}".format(i, houses[i] - 1, costmemoi[i - 1][j][blocks],
                            #                                                               blocks + 2, j))
        ret = float('inf')

        for j in range(n):
            ret = min(ret, costmemoi[m - 1][j][target - 1])

        return ret if ret != float('inf') else -1


sol = Solution()
print(sol.minCost(houses=[0, 0, 0, 0, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(sol.minCost(houses=[0, 2, 1, 2, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2, target=3))
print(sol.minCost(houses=[0, 0, 0, 0, 0], cost=[[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]], m=5, n=2, target=5))
print(sol.minCost(houses=[3, 1, 2, 3], cost=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], m=4, n=3, target=3))
