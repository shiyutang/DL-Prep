class Solution:
    def removeDuplicates(self, nums):
        duplicate = {}
        for i in range(len(nums)-1,-1,-1):
        	if not nums[i] in duplicate:
        		duplicate = {nums[i]:1}
        	elif duplicate[nums[i]] == 1:
        		duplicate[nums[i]] = 2
        	else:
        		del nums[i]
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([]))