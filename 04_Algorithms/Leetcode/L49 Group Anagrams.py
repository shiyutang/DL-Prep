class Solution:
	def groupAnagrams(self, strs):
		Anagramdict  = {}
		result = []
		for strsingle in strs:
			string = list(strsingle)
			string.sort()
			string = ''.join(string)
			if string in Anagramdict:
				result[Anagramdict[string]].append(strsingle)
			else:
				Anagramdict[string] = len(result)
				result.append([strsingle])
		# print(result)

		return result

sol = Solution()
res =sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)


