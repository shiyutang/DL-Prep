class Solution:
	def myPow(self, x,n):
		nnew = abs(n)

		if n < 0:
			return 1/self.fastPow(x,nnew)
		else:
			return self.fastPow(x,nnew)

	def fastPow(self, x,nnew):
		if nnew == 0:
			return 1

		elif nnew%2 == 1:
			return x*self.fastPow(x*x,nnew//2)
		else:
			return self.fastPow(x*x,nnew//2)

sol = Solution()
# res = sol.myPow(2,-10)

res = sol.myPow(2.00000,-2147483648)
print(res)