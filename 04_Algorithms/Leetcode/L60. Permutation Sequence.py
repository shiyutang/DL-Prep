import itertools

class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		a = [str(i+1) for i in range(n)]
		for i,val in enumerate(itertools.permutations(a,n)):
			if i+1 == k:
				return ''.join(list(val))

sol = Solution()
# print(sol.getPermutation(3,3))
print(sol.getPermutation(4,9))
print(sol.getPermutation(4,9))

