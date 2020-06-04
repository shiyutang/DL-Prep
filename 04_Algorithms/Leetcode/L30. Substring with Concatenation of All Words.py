class Solution:
	def findSubstring(self, s, words):
		if words == [[]] or words == []:
			return []

		sLen,wordsLen,wordLen = len(s),len(words),len(words[0])
		words.sort()
		res = []
		for i in range(wordLen):
			start = i
			# print('words',words)
			while start+ wordsLen*wordLen <= sLen:
				piece = s[start:start+wordLen*wordsLen]
				cmpres = []

				for i in range(wordsLen):
					cmpres.append(piece[i*wordLen:(i+1)*wordLen])
				cmpres.sort()
				# print('cmpres',cmpres)
				# print(cmpres == words)
				if cmpres == words:
					res.append(start)

				start += wordLen  
			# 想要进一步迈开步子就得进入piece中，看后面有哪些部分是可以出现得，即应该在word中，同时出现得次数和word相同。

		return res

sol = Solution()
# print(sol.findSubstring("barfoothefoobarman",["foo","bar"]))
# print(sol.findSubstring("wordgoodgoodgoodbestword",["word","good","best","word"]))
print(sol.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",["fooo","barr","wing","ding","wing"]))

