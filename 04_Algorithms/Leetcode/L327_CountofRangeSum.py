class Solution:
    def countRangeSum(self, nums, lower, upper):

        count = 0
        if len(nums) == 1:
            if nums[0]>= lower and nums[0]<=upper:
                return count+1
            else:
                return count
        for i in range(1,len(nums)):
            self.countRangeSum(nums[:i],lower,upper)
            self.countRangeSum(nums[i:],lower,upper)
