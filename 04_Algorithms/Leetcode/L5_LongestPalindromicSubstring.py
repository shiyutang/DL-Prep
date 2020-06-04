class Solution(object):
	"""Manacher"""
	def longestPalindrome(self, s):
		mx,ID = 0, 0
		stmp = '!&'
		for i in range(len(s)):
			stmp = stmp + s[i]+ '&'
		# print(stmp,s)
		p = [0 for i in range(len(stmp))]
		maxLen,maxID = 0,0


		for i in range(len(stmp)):
			if mx>i:
				# print(2*ID-1,len(stmp))
				p[i] = min(p[2*ID-i],mx-i)
			else:
				p[i] = 1
			
			while (i-p[i]>0 and i+p[i]<len(stmp)) and stmp[i+p[i]] == stmp[i-p[i]]:
				p[i] += 1

			if mx<i+p[i]:
				mx = i+p[i]
				ID = i

			if maxLen < p[i]-1:
				maxLen = p[i]-1
				maxID = i
			center = (maxID-maxLen)//2
		# print(center,center+maxLen+1)
		return s[center:center+maxLen]

sol = Solution()
res = sol.longestPalindrome('babad')
print(res)




        
		