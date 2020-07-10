class Solution:
    def numIslands(self, grid) -> int:
        if not grid:
            return 0

        def filter_helper(coord):
            xcoor, ycoor = coord
            if len(grid) > xcoor >= 0 and len(grid[0]) > ycoor >= 0 and grid[xcoor][ycoor] == '1':
                return True
            return False

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop(0)
                        for nei in filter(filter_helper, ((x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1))):
                            stack.append(nei)
                            grid[nei[0]][nei[1]] = '0'
        return cnt


sol = Solution()
# print(sol.numIslands([["1", "1", "1", "1", "0"],
#                       ["1", "1", "0", "1", "0"],
#                       ["1", "1", "0", "0", "0"],
#                       ["0", "0", "0", "0", "0"]]))
#
# print(sol.numIslands([["1", "0", "1", "1", "0"],
#                       ["1", "0", "0", "1", "1"],
#                       ["1", "0", "0", "0", "0"],
#                       ["0", "1", "0", "1", "0"]]))

print(sol.numIslands([["1", "0", "1", "1", "0"],
                      ["1", "0", "0", "1", "1"],
                      ["1", "0", "0", "1", "0"],
                      ["1", "1", "0", "1", "0"],
                      ["1", "0", "1", "1", "0"],
                      ["1", "0", "0", "1", "1"],
                      ["1", "0", "0", "0", "0"],
                      ["0", "1", "0", "1", "0"]]))
