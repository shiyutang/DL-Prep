# class Solution:
# 	def isValidSudoku(self, board):
# 		for i in range(9):
# 			rowlist = [str(k) for k in range(1,10)]
# 			collist = [str(m) for m in range(1,10)]
# 			for j in range(9):
# 				print(board[i][j])
# 				if board[i][j] in rowlist:
# 					rowlist.remove(board[i][j])
# 				elif not board[i][j] == '.':
# 					print('step 1')
# 					return False

# 				print(board[j][i])
# 				if board[j][i] in collist:
# 					collist.remove(board[j][i])
# 				elif not board[j][i] == '.':
# 					print('step 2')
# 					return False


# 		l = [0,3,6,9]
# 		for idx_i in range(len(l)-1):
# 			for idx_j in range(len(l)-1):
# 				blocklist = [str(k) for k in range(1,10)]
# 				for i in range(l[idx_i],l[idx_i+1]):
# 					for j in range(l[idx_j],l[idx_j+1]):
# 						print(board[i][j])
# 						print(blocklist)
# 						if board[i][j] in blocklist:
# 							blocklist.remove(board[i][j])
# 						elif not board[i][j] == '.':
# 							print('step 3')
# 							return False

# 		return True

class Solution:
    def isValidSudoku(self, board):

        row = {}
        col = {}
        block = {}
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y != ".":
                    if (i,y) in row or (j,y) in col or (i//3,j//3,y) in block:
                        return False
                    else:
                        row[i,y] = 1
                        col[j,y] = 1
                        block[i//3,j//3,y] = 1
        return True


sol = Solution()
# board = [["5","3",".",".","7",".",".",".","."],\
#          ["6",".",".","1","9","5",".",".","."],\
#          [".","9","8",".",".",".",".","6","."],\
#          ["8",".",".",".","6",".",".",".","3"],\
#          ["4",".",".","8",".","3",".",".","1"],\
#          ["7",".",".",".","2",".",".",".","6"],\
#          [".","6",".",".",".",".","2","8","."],\
#          [".",".",".","4","1","9",".",".","5"],\
#          [".",".",".",".","8",".",".","7","9"]]
# board = [["8","3",".",".","7",".",".",".","."],\
# 			["6",".",".","1","9","5",".",".","."],\
# 			[".","9","8",".",".",".",".","6","."],\
# 			["8",".",".",".","6",".",".",".","3"],\
# 			["4",".",".","8",".","3",".",".","1"],\
# 			["7",".",".",".","2",".",".",".","6"],\
# 			[".","6",".",".",".",".","2","8","."],\
# 			[".",".",".","4","1","9",".",".","5"],\
# 			[".",".",".",".","8",".",".","7","9"]
# ]
board = [["2","6","3",".","5",".",".","1","."],
		 ["7","4","1","3",".",".",".",".","."],
		 ["9","8","",".",".","6",".",".","4"],
		 ["8",".",".",".",".",".",".","2","."],
		 [".",".","2",".","7",".",".",".","."],
		 [".","1","5",".",".",".",".",".","."],
		 [".",".",".",".",".","2",".",".","."],
		 [".","2",".","9",".",".",".",".","."],
		 [".",".","4",".",".",".",".",".","."]]
result = sol.isValidSudoku(board)
print(result)