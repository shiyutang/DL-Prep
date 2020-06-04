class Solution:
	def longestValidParentheses(self, s):
		stack,point,maxLen,paLen = 0,0,0,0
		paLenStack = []
		if len(s)==0:
			return 0
		while s[0]==')':
			if len(s) == 1:
				return 0
			s = s[1:]

		while point<len(s):
			# print(s[point])
			if paLen>maxLen:
				maxLen = paLen

			if s[point] == '(':
				paLenStack.append(paLen)
				paLen = 0	
				stack += 1
			elif s[point] == ')':
				if stack>0:
					stack -= 1
					paLen = paLen+2+paLenStack.pop(-1)
				else:
					# print(point,s[point])
					paLen = 0
			# print('stack,paLen',stack,paLen)
			point += 1
		if paLen>maxLen:
			maxLen = paLen
		return maxLen

sol = Solution()
# print(sol.longestValidParentheses('(()))()()()'))
# print(sol.longestValidParentheses("()(()"))
print(sol.longestValidParentheses("(()))((()((()))))"))
# print(sol.longestValidParentheses("(()))()()()()()(((((()))))))()()()(((()))(()()()()"))


