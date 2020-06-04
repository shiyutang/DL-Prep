# class Solution:
# 	def singleNumber(self, nums):
# 		a,b = 0,0
# 		for val in nums:
# 			b = (b ^ val) & ~a
# 			a = (a ^ val) & ~b
# 			print('a,b',a,b)
# 		return b

class Solution:
	def singleNumber(self, nums):
		a,b = 0,0
		for c in nums:
			a_current = a&~b&~c | ~a&b&c
			b= ~a&b&~c|~a&~b&c
			a = a_current
			print(a|b,b)
		return b

sol =Solution()
# print(sol.singleNumber([1,3,1,2,1,2,2,3,4,3]))
# print(sol.singleNumber([1,3,2,4,5,3]))
print(sol.singleNumber([0,1,0,1,0,1,99,10,99]))
