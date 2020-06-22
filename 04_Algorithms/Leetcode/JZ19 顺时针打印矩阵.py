# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        rows = [-1, len(matrix)]
        cols = [-1, len(matrix[0])]
        if matrix == [[]] or matrix == []:
            return []

        def isvalid(coord):
            return rows[0] < coord[0] < rows[1] and cols[0] < coord[1] < cols[1]

        def nextcoor(coord, dir):
            if dir == 'right':
                nextCoord = (coord[0], coord[1] + 1)
            elif dir == 'left':
                nextCoord = (coord[0], coord[1] - 1)
            elif dir == 'up':
                nextCoord = (coord[0] - 1, coord[1])
            else:
                nextCoord = (coord[0] + 1, coord[1])

            return nextCoord

        def updateboundary(coord):
            if direction == 'left':
                rows[1] = coord[0]
            elif direction == 'right':
                rows[0] = coord[0]
            elif direction == 'up':
                cols[0] = coord[1]
            else:
                cols[1] = coord[1]

        dir = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
        direction = 'right'
        coordinate = (0, 0)
        ret = [matrix[0][0]]
        while 1:
            if isvalid(nextcoor(coordinate, direction)):
                coordinate = nextcoor(coordinate, direction)
                ret.append(matrix[coordinate[0]][coordinate[1]])
            else:
                updateboundary(coordinate)
                direction = dir[direction]
                if not isvalid(nextcoor(coordinate, direction)):
                    break
        return ret


sol = Solution()
# print(sol.printMatrix([[1, 2, 3, 4],
#                        [5, 6, 7, 8],
#                        [9, 10, 11, 12],
#                        [13, 14, 15, 16]]))

# print(sol.printMatrix([[1, 2, 3, 4],
#                        [5, 6, 7, 8],
#                        [9, 10, 11, 12]]))
print(sol.printMatrix([[]]))