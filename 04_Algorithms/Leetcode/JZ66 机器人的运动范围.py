# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):

        def iscoord(coord):
            if 0 <= coord[0] < rows and 0 <= coord[1] < cols:
                return coord
            return False

        def isvalid(coord):
            coord = (str(coord[0]), str(coord[1]))
            res = 0
            for i in range(len(coord[0])):
                res += int(coord[0][i])
            for j in range(len(coord[1])):
                res += int(coord[1][j])
            if res <= threshold:  # 边界
                return True
            return False

        # BFS 加入合规的
        queue = [(0, 0)]
        marked = [(0, 0)]
        notValid = set()
        cnt = [0, 1][threshold > 0]  # 注意 0,0 也不满足的情况
        while queue:
            coord = queue.pop(0)
            neighbors = [(coord[0] - 1, coord[1]), (coord[0], coord[1] - 1), (coord[0] + 1, coord[1]),
                         (coord[0], coord[1] + 1)]
            # print('neighbors', queue, coord)
            for neigh in map(iscoord, neighbors):
                if neigh and neigh not in marked and neigh not in notValid:
                    if isvalid(neigh):
                        queue.append(neigh)
                        marked.append(neigh)
                        cnt += 1
                    else:
                        notValid.add(neigh)
                # print(neigh, cnt, marked)
        return cnt


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = 5, 10, 10
    # data = -85, 107
    res = sol.movingCount(data[0], data[1], data[2])
    print(res)

    if random_samples:
        import random
        for _ in range(times):
            data = random.randint(3, 10), random.randint(6, 20), random.randint(6, 20)
            print(data)
            res = sol.movingCount(data[0], data[1], data[2])
            print(res)


test(Solution)
