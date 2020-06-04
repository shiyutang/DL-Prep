class Solution:
	def minSubArrayLen(self, s, nums):
		if nums == [] or s> sum(nums):
			return 0
		start,numSum,cnt,minLen = 0,0,0,len(nums)+1
		for num in nums:
			numSum += num
			cnt += 1
			while numSum-nums[start]>=s:
				numSum -= nums[start]
				start += 1
				cnt -= 1

			if numSum >= s:
				minLen = min(cnt,minLen)
				
		return minLen

sol = Solution()
print(sol.minSubArrayLen(7,[2,3,1,2,4,3]))
print(sol.minSubArrayLen(7,[2,4,6,7,2,7,21,5,7,8,3,1,2,4,3]))
print(sol.minSubArrayLen(7,[2,3,1]))
print(sol.minSubArrayLen(7,[2,3,1,2,4,3]))

