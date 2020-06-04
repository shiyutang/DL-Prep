## need to continue with KMP


class Solution:
	def isMatch(self, s, p):
		if not '*' in p: 
			if not len(s)== len(p):
				return False
			for i,letter in enumerate(p):
				if letter == s[i] or letter == '?':
					continue
				elif letter != s[i]:
					return False
			return True
		else:
			if s == '':
				if p == '*' or p == '':
					return True
				else: 
					return False
			starPlace = -2
			sIdx,pIdx,buff= 0,0,0
			while sIdx <len(s):
				# print('sindex:{} starPlace:{} pIdx {}'.format(sIdx,starPlace,pIdx))
				if pIdx ==len(p) :
					# print('step1')
					if pIdx == starPlace:
						return True
					elif not starPlace == -2:
						pIdx = starPlace
					else:
						return False
				elif s[sIdx] == p[pIdx] or p[pIdx] == '?':
					# print('step2')
					if not starPlace == -2:
						buff += 1
					sIdx +=1
					pIdx += 1
				elif p[pIdx] == '*':
					# print('step3')
					pIdx += 1
					starPlace = pIdx
				elif not s[sIdx]== p[pIdx]:
					if not starPlace == -2:
						pIdx = starPlace
						if buff == 0:
							sIdx += 1
						buff = 0
					else:
						return False

			while  pIdx <=len(p)-1 and p[pIdx] == '*':
				pIdx += 1

			if pIdx == len(p):
				return True
			else:
				return False


sol = Solution()
# print(sol.isMatch(s = "aa",p ="*"))
# print(sol.isMatch(s = "a",p ="a******")) # True
# print(sol.isMatch(s = "acdcb",p ="a*c?b")) #False   
# print(sol.isMatch(s = "adceb",p ="a*b")) # True
# print(sol.isMatch(s = "cb",p ="*a"))    #False
# print(sol.isMatch(s = "",p ="*"))        # True
# print(sol.isMatch(s = "aac",p ="*ac"))     # True
print(sol.isMatch(s = "mississippi",p ="m*issip*"))     # True


