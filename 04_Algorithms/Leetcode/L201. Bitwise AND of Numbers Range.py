class Solution(object):
	def rangeBitwiseAnd(self, m, n):
		if n-m >= 1:
			res = '0'
		else:
			return m

		k = 1
		while 2**k <=n :
			print('k = ',k, 2**k,res)
			if 2**k-1 >=m:
				res += '0'
			else:
				res += '1'
			k+=1
		res = res[::-1]
		if res == '':
			return 0
		return int(res,2)

so = Solution()
print(so.rangeBitwiseAnd(5,7))
# print(so.rangeBitwiseAnd(0,2147483647))
# print(so.rangeBitwiseAnd(1,1))
# print(so.rangeBitwiseAnd(1,2))

# print(so.rangeBitwiseAnd(0,0))
# for i in range(100):
# 	for j in range(i+1,100):
# 		print(so.rangeBitwiseAnd(i,j))


