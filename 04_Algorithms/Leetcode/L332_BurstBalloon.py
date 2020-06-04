class Solution(object):
    def maxCoins(self, nums):
        res = 0
        while len(nums)>2:
            minNum = min(nums[1:-1])
            minidx = nums.index(minNum)
            print(minNum)
            res += minNum*nums[minidx-1]*nums[minidx+1]
            print(res)
            nums.remove(minNum)
            print(nums)
        if nums[0]<nums[1]:
            res += nums[1]+nums[0]*nums[1]
        else:
            res +=nums[0]+nums[0]*nums[1]
        print(res)
        return res

sol = Solution()
sol.maxCoins([9,1,5,3,5,4,23,4,2,2,2,4,24,4,11,8])
