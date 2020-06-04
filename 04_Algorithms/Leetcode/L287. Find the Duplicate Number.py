class Solution:
	def findDuplicate(self, nums):
		a,b = 1,0
		for c in nums:
			a = ~a&c|a&~c
			print(a)
		return a

sol= Solution()
print(sol.findDuplicate([4,5,6,4]))

