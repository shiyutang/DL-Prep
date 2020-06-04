class Solution:
	def spiralOrder(self, matrix):
		if matrix == [] or matrix == [[]]:
			return []

		orderList = ['right','down','left','up']
		row,col = 0,0
		posSet = {(row,col)}
		direction = 0
		res = [matrix[0][0]]
		for i in range(len(matrix)*len(matrix[0])-1):
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
			res.append(matrix[row][col])

		return res

sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(sol.spiralOrder([[1,2,3],[5,6,7],[9,10,11],[13,14,15]]))
print(sol.spiralOrder([]))

