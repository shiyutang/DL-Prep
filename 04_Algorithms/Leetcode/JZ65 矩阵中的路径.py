# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        matrix = list(matrix)
        mat = [['' for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = matrix.pop(0)

        # print(mat)

        def isent(ent):
            if 0 <= ent[0] < rows and 0 <= ent[1] < cols:
                return ent
            return False

        def helper(coord, marked, idx):
            if idx == len(path):  # 考虑边界
                return True
            marked.add(coord)
            neighbors = [(coord[0] - 1, coord[1]), (coord[0], coord[1] - 1), (coord[0] + 1, coord[1]),
                         (coord[0], coord[1] + 1)]

            for nei in map(isent, neighbors):    # 回溯：如果没有满足条件的，就返回上一层，访问标记自动恢复
                if nei and nei not in marked and mat[nei[0]][nei[1]] == path[idx]:
                    marked.add(nei)
                    # print(nei, marked, mat[nei[0]][nei[1]], path[idx])
                    res = helper(nei, marked, idx + 1)
                    if res:
                        return res
            return False

        entry = []
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == path[0]:
                    entry.append((i, j))

        for ent in entry:
            marked = set()
            idx = 1
            res = helper(ent, marked, idx)
            if res:
                return res

        return False


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = "ABCESFCSADEE", 3, 4, "ABCCED"
    # data = "A", 1, 1, "A"

    # mat = [['A', 'B', 'C', 'E'],
    #        ['S', 'F', 'C', 'S'],
    #        ['A', 'D', 'E', 'E']]
    res = sol.hasPath(data[0], data[1], data[2], data[3])
    print(res)

    if random_samples:
        import random
        for _ in range(times):
            data = random.randint(3, 10), random.randint(6, 20), random.randint(6, 20)
            print(data)
            res = sol.movingCount(data[0], data[1], data[2])
            print(res)


test(Solution)
