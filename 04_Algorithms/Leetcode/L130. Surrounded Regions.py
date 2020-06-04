class Solution:
	def solve(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		if not board:
		    return
		n, m = len(board), len(board[0])
		boardFilter = lambda x: 0 <= x[0] < n and 0 <= x[1] < m and board[x[0]][x[1]] == 'O'
		## the edge 
		queue = list(filter(boardFilter, [x for i in range(max(n, m)) for x in ((i, 0), (i, m - 1), (0, i), (n - 1, i))]))
		print('queue',queue)

		while queue:
		    x, y = queue.pop()
		    print('x,y',x,y)
		    board[x][y] = 'M'  # such that the thing push into the queue will not repeat
		    print(board)
		    queue.extend(filter(boardFilter, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))
		    print(queue)


		for i in range(n):
			for j in range(m):
				if board[i][j] == 'M':
					board[i][j] = 'O'
				elif board[i][j] == 'O':
					board[i][j] = 'X'
		print(board)

sol = Solution()
# print(sol.solve([["X","X","X","X"],
# 	   			["X","O","O","X"],
# 	   			["X","X","O","X"],
# 	   			["X","O","X","X"]]))
print(sol.solve([["X","O","X","O","X","O"],
	  			["O","X","O","X","O","X"],
	  			["X","O","X","O","X","O"],
	  			["O","X","O","X","O","X"]]))
