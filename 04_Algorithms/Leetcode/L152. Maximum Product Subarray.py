class Solution:
	# def maxProduct(self, nums):
	# 	meetMinus,Positive = False,False
	# 	for i, num in enumerate(nums):
	# 		if num<0:
	# 			if meetMinus:
	# 				nums[MinusIndex] = -nums[MinusIndex]
	# 				nums[i] = -nums[i]
	# 				meetMinus = False

	# 			else:
	# 				meetMinus,MinusIndex = True,i
	# 		elif num == 0:
	# 			meetMinus = False

	# 	print(nums)
		
	# 	for num in nums:
	# 		if num>0:
	# 			Positive = True

	# 	tmpProduct,maxProduct = 1,-100000000
	# 	for i,num in enumerate(nums):

	# 		if num >0:
	# 			tmpProduct = tmpProduct*num
	# 			if tmpProduct>maxProduct:
	# 				maxProduct = tmpProduct
	# 		elif num < 0 and not Positive:
	# 			# print('in')
	# 			tmpProduct = tmpProduct*num
	# 			if tmpProduct>maxProduct:
	# 				maxProduct = tmpProduct
	# 		else:
	# 			tmpProduct = 1
	# 			curProduct = 0
	# 			if curProduct>maxProduct:
	# 				maxProduct = curProduct

	# 		# print(tmpProduct)

	# 	return maxProduct

## 最大乘积往前乘就行了，只是在有负数的时候需要考虑取前一部分的负数还是后一部分的。
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        print(A,B,A+B)
        return max(A + B)

sol = Solution()
# print(sol.maxProduct([2,3,-2,4]))
# print(sol.maxProduct([-2,0,-1]))
# print(sol.maxProduct([2,0,1]))
print(sol.maxProduct([2,-5,0,-6,-4,3]))