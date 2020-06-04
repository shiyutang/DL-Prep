class Solution:
	def maxSubArray(self, nums):
		queue = []
		maxval = -10000000
		queueSum = 0
		if max(nums)<0:
			return max(nums)
		for num in nums:
			if num+queueSum>0:
				queue.append(num)
				queueSum+=num
				if queueSum>maxval:
					maxval = queueSum
			else:
				queue = []
				queueSum = 0

		return maxval if maxval>-10000000 else 0

sol = Solution()
# print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
# print(sol.maxSubArray([]))
# print(sol.maxSubArray([-3,1,2,3,-4,3,4,-5,6,-2,-1,3,-2]))
print(sol.maxSubArray([-1]))
print(sol.maxSubArray([-8,-8,3,-8,-8]))



