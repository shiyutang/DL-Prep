class Solution(object):
	"""3 for loops to find all combs 
	do not use dictionary but list
	try to use +[] rather than append()"""
	def letterCombinations(self,digits):
		res = []
		numCodeBook = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 
					   6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
		if digits == '':
			return []
		else:
			comb = ['']
		for digit in digits:
			combtmp = []		
			for res in comb:
				for ch in numCodeBook[int(digit)]:
					combtmp+= [res+ch]
				# print(combtmp)
			comb = combtmp
		return comb		

sol = Solution()
res = sol.letterCombinations('23')
print(res)
		