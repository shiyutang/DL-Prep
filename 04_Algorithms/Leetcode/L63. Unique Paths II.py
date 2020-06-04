class Solution:
	def uniquePathsWithObstacles(self,  obstacleGrid):
		if obstacleGrid == [] or obstacleGrid == [[]]:
			return 0

		m,n = len(obstacleGrid),len(obstacleGrid[0])

		memoi = [[0]* n for _ in range(m)]
		for ii in range(n):
			if not obstacleGrid[0][ii] == 1:
				memoi[0][ii] = 1
			else:
				break

		for jj in range(m):
			if not obstacleGrid[jj][0] == 1:
				memoi[jj][0] = 1
			else:
				break

		if m >= 2 and n >=2:
			for i in range(1,m):
				for j in range(1,n):
					if obstacleGrid[i][j] == 1:
						memoi[i][j] = 0
					else:
						memoi[i][j] = memoi[i-1][j] + memoi[i][j-1]

		return memoi[-1][-1]


sol = Solution()
print(sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
