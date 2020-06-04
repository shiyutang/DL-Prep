class Solution:
    def firstMissingPositive(self, nums):
        if nums == []:
            return 1
        maxval = max(nums)
        if  maxval<=0:
            return 1
        

        for i in (i for i in range(1,maxval+2)):
            if not i in nums:
                return i

sol = Solution()
result = sol.firstMissingPositive([5])
print(result)            