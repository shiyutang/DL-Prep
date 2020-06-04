class Solution:
    def updateMatrix(self, matrix):
        updateMat = [[10 ** 10 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        # row, col = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    updateMat[i][j] = 0
                else:
                    if not (i == 0 and j == 0):
                        possible = []
                        idx = [i, j]
                        for index in [[idx[0] - 1, idx[1]], [idx[0], idx[1] - 1]]:
                            if index[0] >= 0 and index[0] < len(matrix) and index[1] >= 0 and index[1] < len(
                                    matrix[0]):  # index is valid
                                possible.append(updateMat[index[0]][index[1]] + 1)
                        updateMat[i][j] = min(possible)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == 0:
                    updateMat[i][j] = 0
                else:
                    if not (i == len(matrix) - 1 and j == len(matrix[0]) - 1):
                        possible = []
                        idx = [i, j]
                        for index in [[idx[0] + 1, idx[1]], [idx[0], idx[1] + 1]]:
                            if index[0] >= 0 and index[0] < len(matrix) and index[1] >= 0 and index[1] < len(
                                    matrix[0]):  # index is valid
                                possible.append(updateMat[index[0]][index[1]] + 1)
                        updateMat[i][j] = min(min(possible), updateMat[i][j])
        print(updateMat)
        return updateMat

sol = Solution()
# sol.updateMatrix([[0],[0],[0],[0],[0]])
# sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
# sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
# sol.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
sol.updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]])