class Solution:
    def permute(self, nums):
    	self.result = []
		self.dfs(nums,[],self.result)

    def dfs(self, nums, prefix, result):
    	if nums == []:
    		self.result.append(prefix)
    	else:
    		for i in range(len(nums)):
    			self.dfs(nums[0:i]+nums[i+1:],self.prefix+[nums[i]],self.result)

import itertools

class Solution:
    def permute(self, nums):
        res = []
        if nums == []:
            return [[]]
        for i in itertools.permutations(nums, len(nums)):
            res.append(i)
            
        return res

sol = Solution()
result = sol.permute()
print(result)