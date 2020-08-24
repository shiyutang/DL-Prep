import numpy as np


def road(weights):
    memoi = np.zeros(len(weights), len(weights[0]))

    def legal(coords):
        return len(weights) >= coords[0] >= 0 and len(weights[0]) >= coords[1] >= 0

    for row in range(len(weights)):
        for col in range(len(weights[0])):
            cur = weights[row][col]
            if row == 0 and col == 0:
                memoi[row][col] = cur
            else:
                up, left = (row - 1, col), (row, col - 1)
                res = float('inf')
                if legal(up):
                    res = min(res, memoi[up[0]][up[1]] + cur)
                if legal(left):
                    res = min(res, memoi[left[0]][left[1]] + cur)
                memoi[row][col] = res

    return memoi[-1][-1]


a = [[1, 4, 3], [2, 3, 4], [4, 5, 1]]
print(road(a))
