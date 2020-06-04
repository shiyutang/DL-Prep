class Solution:
	def simplifyPath(self, path: str) -> str:
		path = path.split('/')
		# print(path)
		res = []
		for val in path:
			if val == '' or val == '.':
				continue
			elif val == '..':
				if len(res)>0:
					res.pop(-1)
			else:
				res.append(val)
		# print(res)
		resStr = ''
		if res==[]:
			res.append('')
		for item in res:
			resStr+='/'+item

		return resStr


sol = Solution()
# print(sol.simplifyPath("/a//b////c/d//././/..")) # /a/b/c
# print(sol.simplifyPath("/a/../../b/../c//.//")) # "/c"
# print(sol.simplifyPath("/a/./b/../../c/")) # "/c"
# print(sol.simplifyPath("/home////")) # "/c"
print(sol.simplifyPath("/../")) # "/c"





