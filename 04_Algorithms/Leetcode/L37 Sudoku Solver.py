class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        self.board = board
        return self.solve()
        
    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1
        
    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True,self.board
                       
        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True,self.board
                self.board[row][col] = '.'
        
    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))            
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe
    
    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)

sol = Solution()
board = [["5","3",".",".","7",".",".",".","."],\
         ["6",".",".","1","9","5",".",".","."],\
         [".","9","8",".",".",".",".","6","."],\
         ["8",".",".",".","6",".",".",".","3"],\
         ["4",".",".","8",".","3",".",".","1"],\
         ["7",".",".",".","2",".",".",".","6"],\
         [".","6",".",".",".",".","2","8","."],\
         [".",".",".","4","1","9",".",".","5"],\
         [".",".",".",".","8",".",".","7","9"]]
flag, board = sol.solveSudoku(board)
print(flag,board)