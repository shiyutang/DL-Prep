N = int(input())
data = []
for i in range(N):
    tmp = list(map(int, input().split(' ')))
    data.append(tmp)


def solution(matrix):
    if not matrix:
        return 0

    def isvalid(coor):
        x, y = coor
        return len(matrix) > x >= 0 and len(matrix[0]) > y >= 0

    cache = [[1e10 for _ in range(len(matrix))] for __ in range(len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == 0 and col == 0:
                cache[row][col] = 0
            for nei in filter(isvalid, ((row - 1, col), (row, col - 1))):
                cache[row][col] = min(cache[row][col],
                                      cache[nei[0]][nei[1]] + abs(matrix[nei[0]][nei[1]] - matrix[row][col]))

    # for row in range(len(matrix)):
    #     for col in range(len(matrix[0])):
    #         if row == 0 and col == 0:
    #             continue
    #         for nei in filter(isvalid, ((row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1))):
    #             # print(nei)
    #             cache[row][col] = min(cache[row][col],
    #                                   cache[nei[0]][nei[1]] + abs(matrix[nei[0]][nei[1]] - matrix[row][col]))

    return cache[row][col]


print(solution(data))
#
# 3
# 1 2 4
# 1 3 1
# 1 2 1
