class Solution:
    def singleNumber(self, nums):
    	for num in nums[1:]:
    		nums[0] = nums[0]^num
    	return nums[0]

sol = Solution()
print(sol.singleNumber([1,2,1,2,3,4,5,4,3]))
print(sol.singleNumber([1,-2,1,-2,0,4,5,4,0]))
