class Solution:
    def searchMatrix(self, matrix, target):
        rows,cols,row,col = len(matrix),len(matrix[0]),0,len(matrix[0])-1
        while row < rows and col>=0:
            if target> matrix[row][col]:
                row += 1
            elif target< matrix[row][col]:
                col -= 1
            else:
                return True
        return False

sol = Solution()
# res = sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],
#                   [3,6,9,16,22],[10,13,14,17,24],
#                   [18,21,23,26,30]],33)
# print(res)
# res = sol.searchMatrix([[25,28,33]],33)
# print(res)
# res = sol.searchMatrix([[-1,3]],1)
# print(res)
# res = sol.searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]],13)
# print(res)
res = sol.searchMatrix([[-5]],-10)
print(res)