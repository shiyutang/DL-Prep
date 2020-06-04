# shouldn't use DFS for this


class Solution:
    def findzero(self,matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0:
                    return [i,j]


    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        stack = []
        stack.append(self.findzero(matrix))
        # mark = [[False * len(matrix[0])]*len(matrix[1])]
        updateMat = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix[1]))]
        countdis0 = 0
        while stack != []:
            idx = stack.pop()
            if matrix[idx[0]][idx[1]] != 0:
                countdis0 += 1
            updateMat[idx[0]][idx[1]] = countdis0
            for index in [[idx[0]+1,idx[1]],[idx[0]-1,idx[1]],[idx[0],idx[1]+1],[idx[0],idx[1]-1]]:
                if index[0]>=0 and index[0]<len(matrix) and index[1]>=0 and index[1]<len(matrix[0]):  #index is valid
                    if updateMat[index[0]][index[1]] == -1: # value remain not visited
                        stack.append(index)
        return updateMat

sol = Solution()
sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
