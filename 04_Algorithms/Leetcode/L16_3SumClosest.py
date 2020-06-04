class Solution(object):
	"""keep one still and adjust the rest"""
	def threeSumClosest(self, nums, target):
		nums.sort()
		result = nums[-1]+nums[-2]+nums[-3]
		for i in range(len(nums)-2):
			j,k = i+1,len(nums)-1
			while j<k:
				numSum = nums[i]+nums[j]+nums[k]
				if numSum == target:
					return numSum
				elif numSum>target:
					k -= 1
				else:
					j += 1
				if abs(numSum-target)<abs(result-target):
					result = numSum
		return result




sol = Solution()
result = sol.threeSumClosest(nums =[-1, 2, 4,2,5,2,4,1,5,21,3,5,1,3,13,3,41, -4] ,target = 12)
result = sol.threeSumClosest(nums =[1,1,1,0] ,target = -100)

print(result)