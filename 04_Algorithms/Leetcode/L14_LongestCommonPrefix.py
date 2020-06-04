class Solution:
    def longestCommonPrefix(self, strs):
    	common = ''
    	if strs == [] or strs == [""]:
    		return common
    	cnt = min(len(str) for str in strs)
    	for i in range(cnt):
    		c = strs[0][i]
    		for str in strs:
    			if str[i] != c:
    				return common
    		common += c
    	return common

sol = Solution()
# res = sol.longestCommonPrefix(["dog","racecar","car"])
# res = sol.longestCommonPrefix(["flower","flow","flight"])
# res = sol.longestCommonPrefix(['fdsf','fdsd','fdsrwdf'])
res = sol.longestCommonPrefix(['a'])

print(res)

        