class Solution:
	def minPathSum(self, grid):
		if grid == [] or grid == [[]]:
			return 0
		m,n = len(grid),len(grid[0])
		memoi = [[0]* n for _ in range(m)]
		for i in range(m):
			for j in range(n):
				if i == 0:
					if j == 0:
						memoi[i][j] = grid[i][j]
					else:
						memoi[i][j] = memoi[i][j-1]+grid[i][j]
				elif j == 0:
					memoi[i][j] = memoi[i-1][j]+grid[i][j]
				else:
					if memoi[i-1][j]<memoi[i][j-1]:
						memoi[i][j] = memoi[i-1][j]+grid[i][j]
					else:
						memoi[i][j] = grid[i][j] +memoi[i][j-1] 
				# print(memoi)

		return memoi[-1][-1]

sol = Solution()
print(sol.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))