class Solution:
	def exist(self, board, word):
		self.m,self.n = len(board),len(board[0])
		self.board = board
		res = []
		visited = {}
		for i,row in enumerate(board):
			for j, item in enumerate(row):

				if board[i][j] == word[0]:
					# print(i,j,board[i][j],word)
					res.append(self.match(word,i,j,visited))
		return [False,True][any(res)]


	def match(self,word,i,j,visited):
		# print(word,i,j)
		if len(word) == 0:
			# print('RETURN True')

			return True
		# if word == 'AAB' and (i,j) == (1,1):
			# print(word[0],self.board[i][j],visited)
		if i<0 or i>=self.m or j <0 or j>= self.n or not word[0] == self.board[i][j] or ((i,j) in visited and visited[(i,j)]) :
			# print('RETURN False')
			return False
		else:
			visited[(i,j)] = True
			res = self.match(word[1:],i+1,j,visited) or self.match(word[1:],i,j+1,visited)\
				or self.match(word[1:],i-1,j,visited) or self.match(word[1:],i,j-1,visited)
			visited[(i,j)] = False

		return res

sol = Solution()
# board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# print(sol.exist(board,'ABCCED'))
# print(sol.exist(board,'SEE'))
# print(sol.exist(board,'ABCB'))

board = [["C","A","A"],
		 ["A","A","A"],
		 ["B","C","D"]]
print(sol.exist(board,"AAB"))