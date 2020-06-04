class Solution:
	def lengthOfLIS(self, nums):
		if nums == []:
			return 0
		prevSmallBuff =[0 for _ in range(len(nums))]
		for i,numNow in enumerate(nums):
			for j,numprev in enumerate(nums[:i]):
				if numprev<numNow:
					prevSmallBuff[i] = max(prevSmallBuff[j]+1,prevSmallBuff[i])

		return max(prevSmallBuff)+1

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS([]))
print(sol.lengthOfLIS([10,9,8,7,6,5,4,3,2,1]))
print(sol.lengthOfLIS([3,54,7,62,5,5,3,36,2,2,35,2,7,5,8,687]))

            