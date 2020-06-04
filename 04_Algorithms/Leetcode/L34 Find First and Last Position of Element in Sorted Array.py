class Solution:
	def search(self, nums, target):

		if not target in nums:
			return [-1,-1]
		else:
			target = (target-0.5,target+0.5)
			start,end = self.binary_search(nums,target[0]),\
						self.binary_search(nums,target[1])
		return [start, end-1] 

	def binary_search(self,nums,target):
		print(target)
		mediumIdx = len(nums)//2
		medium = nums[mediumIdx]
		print('medium',medium,mediumIdx)
		if target > medium:
			if mediumIdx+1==len(nums) or target < nums[mediumIdx+1]:
				print('step 1')
				return mediumIdx+1 
			else:
				print('step 2')
				print('nums[mediumIdx+1:]',nums[mediumIdx+1:])
				return self.binary_search(nums[mediumIdx+1:],target)+mediumIdx+1
		else:
			if mediumIdx -1 == -1 or target > nums[mediumIdx-1]:
				print('step 3')
				return mediumIdx
			else: 
				print('step 4')
				return self.binary_search(nums[0:mediumIdx],target)




sol = Solution()
# result = sol.search([11,12,13,2,3,4,5,6,7,8],2)
# result = sol.search([4,5,6,7,0,1,2],0)
result = sol.search([5,5,5,5,5,5,5,5,5,5,5],25)
# result = sol.search([5,6,6,6,6,6,6,6,7,7,8,8,10],6)
print(result)
            
        