class Solution:
    def minReorder(self, n: int, connections) -> int:
        reachableset = {0}
        cnt = 0
        while len(reachableset) < n:
            for ele in connections:
                if ele[1] in reachableset:
                    reachableset.add(ele[0])
                elif ele[0] in reachableset:
                    reachableset.add(ele[1])
                    cnt += 1

        return cnt


sol = Solution()
print(sol.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
print(sol.minReorder(n=5, connections=[[1, 0], [1, 2], [3, 2], [3, 4]]))
print(sol.minReorder(n=3, connections=[[1, 0], [2, 0]]))
