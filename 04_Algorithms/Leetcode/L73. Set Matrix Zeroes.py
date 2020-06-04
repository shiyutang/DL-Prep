class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix),len(matrix[0])
        rowSet,colSet = set(),set()
        for i in range(m):
        	for j in range(n):
        		if matrix[i][j] == 0:
        			rowSet.add(i)
        			colSet.add(j)

        for row in rowSet:
        	for j in range(n):
        		matrix[row][j] = 0

        for i in range(m):
        	for col in colSet:
        		matrix[i][col] = 0

        print(matrix)

sol = Solution()
sol.setZeroes([
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
])
sol.setZeroes([
  [1,1,1],
  [1,0,1],
  [1,1,1]
])