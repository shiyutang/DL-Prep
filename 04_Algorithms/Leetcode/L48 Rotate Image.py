class Solution1:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matLen = len(matrix)
        padding = 0

        def rotatePeri(matrix, padding, matLen):
            removelist = []
            for i in range(padding + 1, matLen - padding):
                removelist.append(matrix[padding][i])
            # print(len(removelist),matLen-2*padding)

            for i in range(matLen - 2 * padding - 1):
                end = matLen - padding - 1

                matrix[padding][end - i] = matrix[padding + i][padding]  # 0~N-1
                matrix[i + padding][padding] = matrix[end][i + padding]
                matrix[end][i + padding] = matrix[end - i][end]
                matrix[end - i][end] = removelist.pop(-1)
            # print('padding,end', padding,end)

        while matLen - 2 * padding > 1:
            rotatePeri(matrix, padding, matLen)
            padding += 1
            print('matrix', matrix)

# 旋转之后的结果就是每列从下到上-》每行从左到右
# zip 是按照每列操作，因此就相当于转置了
class Solution:
    def rotate(self, matrix):
        matrix[:] = zip(*matrix)  # 以矩阵中每列解压之后进行打包，等效于转置
        print(matrix)
        for i in range(len(matrix)):  # 每行等于行的求反得到结果
            matrix[i] = list(matrix[i])[::-1]
        print(matrix)

# method3: 可以转置之后再反转每一行元素

sol = Solution()
sol.rotate([[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]])
sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sol.rotate([[]])
