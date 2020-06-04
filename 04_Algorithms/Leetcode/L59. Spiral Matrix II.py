class Solution:
	def generateMatrix(self, n):
		single = [0 for i in range(n)]
		matrix = []
		for i in range(n):
			single = []
			for j in range(n):
				single.append(0)
			matrix.append(single)
		
		orderList = ['right','down','left','up']
		row,col = 0,0
		posSet = {(row,col)}
		matrix[row][col] = 1
		direction = 0
		for i in range(1, n**2):
			if direction == 0:
				row,col = row,col+1
				if col>=len(matrix[0]) or (row,col) in posSet:
					direction += 1
					row,col = row+1,col-1
			elif direction == 1:
				row,col = row+1,col
				if row>=len(matrix) or (row,col) in posSet:
					direction+=1
					row,col = row-1,col-1
			elif direction ==2:
				row,col = row,col-1
				if col<0 or (row,col) in posSet:
					direction+=1
					row,col = row-1,col+1
			else:
				row,col = row-1,col

				if (row,col) in posSet:
					direction = 0
					row,col = row+1,col+1
			posSet.add((row,col))
			matrix[row][col] = i+1
		# print(matrix)

		return matrix

sol = Solution()
print(sol.generateMatrix(1))