import copy
class Solution:
    def updateMatrix(self, matrix):
        updateMat = [[1000**100 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        mark = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    mark[i][j] = True
                    queue = []
                    queue.append([[i, j], 0])
                    marks = copy.deepcopy(mark)
                    while queue != []:
                        idx, depth = queue.pop(0)
                        if depth<updateMat[idx[0]][idx[1]]:
                            updateMat[idx[0]][idx[1]] = depth
                        marks[idx[0]][idx[1]] = True
                        for index in [[idx[0] + 1, idx[1]], [idx[0] - 1, idx[1]], [idx[0], idx[1] + 1],[idx[0], idx[1] - 1]]:
                            if index[0] >= 0 and index[0] < len(matrix) and index[1] >= 0 and index[1] < len(matrix[0]):  # index is valid
                                if matrix[index[0]][index[1]] == 0:
                                    continue
                                if marks[index[0]][index[1]] == False:
                                    marks[index[0]][index[1]] = True
                                    queue.append([index,depth+1])
        # print(updateMat)
        return updateMat

sol = Solution()
# sol.updateMatrix([[0],[0],[0],[0],[0]])
# sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
# sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
sol.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
