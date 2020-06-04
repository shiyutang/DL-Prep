## use bit to represent letter to save space,use dict to save time

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        def string2num(string):
        	res = ''
        	for s in string[:]:
        		if s == 'A':
        			res += '00'
        		elif s == 'C':
        			res += '01'
        		elif s == 'G':
        			res += '10'
        		elif s == 'T':
        			res += '11'
        	return int(res,2)

        freqDict = {}
        result = []
        for i in range(len(s)-9):
        	stringId = string2num(s[i:i+10])
        	# print(freqDict)
        	if not stringId in freqDict:
        		freqDict[stringId] = 1
        	else:
        		if freqDict[stringId] == 1:
        			result.append(s[i:i+10])
        		freqDict[stringId] += 1
        return result


sol = Solution()
# print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# print(sol.findRepeatedDnaSequences(""))
print(sol.findRepeatedDnaSequences("AAAAAAAAAAAA"))


