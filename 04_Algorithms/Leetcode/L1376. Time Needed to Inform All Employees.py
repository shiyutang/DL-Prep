from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: list, informTime: list) -> int:
        head2child = defaultdict(list)
        for idx, leader in enumerate(manager):
            head2child[leader].append(idx)

        def helper(leaderID):
            res = 0
            if leaderID not in head2child:
                return 0

            for ele in head2child[leaderID]:   # dfs 先左子再右子，不断向下，并取最大，不需要存储
                childres = helper(ele) + informTime[leaderID]
                res = max(res, childres)
            return res

        return helper(headID)


sol = Solution()
data = 7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]
data = 15, 0, [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
data = 4, 2, [3, 3, -1, 2], [0, 0, 162, 914]
data = 6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]
data = 1, 0, [-1], [0]
rs = sol.numOfMinutes(data[0], data[1], data[2], data[3])
print(rs)
