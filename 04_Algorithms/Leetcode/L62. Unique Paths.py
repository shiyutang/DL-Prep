class Solution:
	def uniquePaths(self, m, n):
		self.memo = [[0]* n for _ in range(m)]

		def countMemo(m,n):
			if n == 1 or m == 1:
				self.memo[m-1][n-1] = 1
				return 1
			elif n == 2:
				self.memo[m-1][n-1]=m
				return m
			elif m == 2:
				self.memo[m-1][n-1] = n
				return n
			else:
				# print('(m,n),memo',(m,n),memo)
				if not self.memo[m-1][n-1]==0:
					# print('in')
					return self.memo[m-1][n-1]
				else:
					res = 0
					for i in range(1,m+1):
						self.memo[i-1][n-2] = countMemo(i,n-1)
						# print((i,n-1),self.memo[i-1][n-2])
						res += self.memo[i-1][n-2]

					self.memo[m-1][n-1] = res
					# print('memo')

					return res

		return countMemo(m,n)
		

## 当前选择数目为左右选择得到的数目之和

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memoi = [[0]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memoi[i][j] = 1
                else:
                    memoi[i][j] = memoi[i-1][j] + memoi[i][j-1]
        return memoi[-1][-1]


sol = Solution()
# print(sol.uniquePaths(7,3)) #28
print(sol.uniquePaths(100,100))  #22750883079422934966181954039568885395604168260154104734000
# print(sol.uniquePaths(10,10))  # 48620
# print(sol.uniquePaths(5,5))
# print(sol.uniquePaths(23,12)) # 193536720



