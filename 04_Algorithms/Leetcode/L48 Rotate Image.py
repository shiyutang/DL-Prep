class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matLen = len(matrix)
        padding = 0
        def rotatePeri(matrix,padding,matLen):
        	removelist = []
        	for i in range(padding+1,matLen-padding):
        		removelist.append(matrix[padding][i])
        	# print(len(removelist),matLen-2*padding)

        	for i in range(matLen-2*padding-1):
        		end = matLen-padding-1

        		matrix[padding][end-i] = matrix[padding+i][padding] # 0~N-1
        		matrix[i+padding][padding] = matrix[end][i+padding]
        		matrix[end][i+padding] = matrix[end-i][end]
        		matrix[end-i][end] = removelist.pop(-1)
        		# print('padding,end', padding,end)

        while matLen-2*padding>1:
        	rotatePeri(matrix,padding,matLen)
        	padding += 1
        	print('matrix', matrix)

sol = Solution()
# sol.rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
sol.rotate([[]])