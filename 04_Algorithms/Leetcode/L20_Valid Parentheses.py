# class Solution(object):
# 	"""!! the parenthesis may not be symetric"""
# 	def isValid(self, s):
# 		pairs = {'{':'}', '(':')', '[':']','':''}
# 		backs = [')','}',']']
# 		if len(s) %2 == 1:
# 			return False
# 		if s == '':
# 			return True
# 		part1 = s[:len(s)//2]
# 		part2 = s[len(s)//2:]
# 		# print(part1,part2)
# 		if len(part1) == 1 and len(part2) == 1:
# 			if part1[-1] in backs or part2 != pairs[part1]:
# 				return False
# 			else:
# 				return True
# 		if (len(part2)%2 == 1):
# 			# print('part of me is odd')
# 			# print(part1[-1],part2[0])
# 			if part1[-1] in backs or pairs[part1[-1]] != part2[0]:
# 				# print('and I am not equal with the other half')
# 				return False
# 			else:
# 				# print('keep checking')
# 				return self.isValid(part1[:-1]+part2[1:])
# 		else:
# 			# print('part of me is even')
# 			if part1[-1] in backs or pairs[part1[-1]] != part2[0]:
# 				# print('not equal,keep checking')
# 				return self.isValid(part1) and self.isValid(part2)
# 			else:
# 				# print('equal and combine')
# 				# print(part1[:-1]+part2[1:])
# 				return self.isValid(part1[:-1]+part2[1:])

class Solution(object):
    """!! the parenthesis may not be symetric
    restrained by the recursive thought"""

    def isValid(self, s):
        pairs = {'{': '}', '(': ')', '[': ']', '': ''}
        backs = [')', '}', ']']
        if len(s) % 2 == 1:
            return False
        if s == '':
            return True
        for i, ch in enumerate(s):
            if ch in backs:
                # print(ch,s[i-1])
                if i - 1 < 0 or pairs[s[i - 1]] != ch:
                    return False
                else:
                    return self.isValid(s[:i - 1] + s[i + 1:])
        return False


class Solution:
    '''solution from leetcode
    by using stack deal and pop is much simple
    don't have to start over each time change s'''

    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return not stack


sol = Solution()
res = sol.isValid("[()]")
print(res)
res = sol.isValid("{[()]}")
print(res)
res = sol.isValid("[](){}")
print(res)
res = sol.isValid("[]{}")
print(res)
res = sol.isValid("[]")
print(res)
res = sol.isValid('([)]')
print(res)
res = sol.isValid(')(')
print(res)
res = sol.isValid('((')
print(res)

res = sol.isValid("(([]){})")
print(res)
res = sol.isValid("")
print(res)
