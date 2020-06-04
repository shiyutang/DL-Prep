class Solution:
	def searchMatrix(self, matrix, target):
		if matrix == [[]] or matrix == []:
			return False
		NoRows,NoCols = len(matrix),len(matrix[0])
		print(NoRows,NoCols)

		first = []
		for i in range(NoRows):
			first.append(matrix[i][0])

		for i in range(NoRows):
			if target <= first[i]:
				pos = i-1
				break
			elif i == NoRows-1:
				pos = NoRows-1



		if not pos == NoRows-1 and target == first[pos+1]:
			return True
		else:
			colPos = 0
			targetRow = matrix[pos]
			for j in range(NoCols):
				if targetRow[j] == target:
					return True

			return False



sol = Solution()
print(sol.searchMatrix([ [1,   3,  5,  7],
						 [10, 11, 16, 20],
						 [23, 30, 34, 50]],35))



