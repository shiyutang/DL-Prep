class Solution(object):
	"""seperate and combine
	could use a more refined scale: 1 4 5 9 etc
	which means bigger and substract"""
	def intToRoman(self, num):
		numList = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
		numRomanDict = {1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL',
						50:'L', 90:'XC', 100:'C', 400:'CD', 500:'D',
						900:'CM', 1000:'M'}
		sepnum = []
		res = ''
		for i in range(len(str(num))-1,-1,-1):
			sep = (num//(10**i))%10
			sepnum.append(sep)
			if sep == 1 or sep == 4 or sep == 5 or sep == 9:
				res += numRomanDict[sep*(10**i)]
			elif sep < 4:
				res += numRomanDict[(10**i)]*sep
			elif sep>5:
				res += numRomanDict[5*(10**i)] + numRomanDict[(10**i)]*(sep-5)

		print(sepnum)
		return res

sol = Solution()
res =  sol.intToRoman(1994)
print(res)


	