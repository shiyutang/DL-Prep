class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
        	for j in range(i+1,len(nums)):
        		if nums[i]+nums[j]==target:
        			return [i,j]


# class Solution:                        # infor: only two nums add together 
#     def twoSum(self, nums,target):
#         num2indices = {}
#         for k, num in enumerate(nums):
            
#             remain = target - num
#             if remain in num2indices:
#                 return [num2indices[remain], k]
            
#             num2indices[num] = k
            
        
#         return []

sol = Solution()
# res = sol.twoSum(nums = [2,3,7,8,11,15], target = 15)
res = sol.twoSum(nums = [0,4,3,0], target = 0)
print(res)
