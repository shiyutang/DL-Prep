# 不断向direction 索引矩阵并放入ret，
# 当碰到边（contain state） 转变方向
# 直到转到的方向也是边
class Solution:
    def spiralOrder(self, matrix) -> list:
        state = 0
        direction = 'right'
        ret = []
        coordinate = (0, 0)
        directionChange = {'right': 'down', 'down': 'left',
                           'left': 'up', 'up': 'right'}

        def plus(coor, num):
            coor = list(coor)
            if direction == 'right':
                coor[1] += num
            elif direction == 'down':
                coor[0] += num
            elif direction == 'left':
                coor[1] -= num
            elif direction == 'up':
                coor[0] -= num
            return tuple(coor)

        def viable(coor):
            coor = plus(coor, state)
            return len(matrix) > coor[0] >= 0 and len(matrix[0]) > coor[1] >= 0

        while viable(coordinate):
            ret.append(matrix[coordinate[0]][coordinate[1]])
            if not viable(plus(coordinate, 1)):
                direction = directionChange[direction]
                if direction == 'up':
                    state += 1
                coordinate = plus(coordinate, 1)
            else:
                coordinate = plus(coordinate, 1)

        return ret


sol = Solution()
print(sol.spiralOrder([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]
                       ]))
print(sol.spiralOrder([]))

print(sol.spiralOrder([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]]))
