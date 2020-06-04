# class Solution:
# 	def removeDuplicates(self, nums):
# 		if nums == []:
# 			return 0

# 		listLen = len(nums) 
# 		i = listLen-2
# 		pre = nums[-1]
# 		returnLen = 1

# 		while i>=0:
# 			cur = nums[i]
# 			if not cur == pre:
# 				returnLen += 1
# 				pre = nums[i]
# 			else:
# 				nums.pop(i)
# 				pre = nums[i]
# 			i -= 1


# 		return returnLen

class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums) < 2:
            return len(nums)
    
        j = 0
        
        for num in nums[1:]:
            if num != nums[j]:
                j += 1
                nums[j] = num
        return j+1,nums

sol = Solution()
res,nums = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(res,nums)

