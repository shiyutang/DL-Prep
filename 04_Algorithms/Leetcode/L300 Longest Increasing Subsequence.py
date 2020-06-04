class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1
        result = {nums[0]: 1}
        for i in range(1, len(nums)):
            maxLen = 1
            for key in result:
                if nums[i] > key:
                    maxLen = max(maxLen, result[key] + 1)
            result[nums[i]] = maxLen
            # print(result)
        for key in result:
            maxLen = max(result[key], maxLen)
        return maxLen


# version 2
class SolutionV2:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        prevSmallBuff = [0 for _ in range(len(nums))]
        for i, numNow in enumerate(nums):
            for j, numprev in enumerate(nums[:i]):
                if numprev < numNow:
                    prevSmallBuff[i] = max(prevSmallBuff[j] + 1, prevSmallBuff[i])

        return max(prevSmallBuff) + 1


# version 3: 24 ms, nlogn
# 如果能达到相同的序列积累效果，那么就可以直接替换
import sys
import bisect


class SolutionV3:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [sys.maxsize for _ in range(n)]
        res = 0
        for num in nums:
            i = bisect.bisect_left(dp, num)  # 返回 num 在 dp 中插入的位置
            dp[i] = num  # 把第 i 个替换为 num
            if i == res:  # num 插入的位置和积累的相同，则积累加1
                res += 1
            print(dp)
        return res


# test
def test(method, random_samples=False):
    # test settings
    times = 100

    sol = method()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(nums, end=' ')
    res = sol.lengthOfLIS(nums)
    print(' and the LIS is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num = random.randint(0, 200)
                nums.append(num)
            print(nums, end=' ')
            res = sol.lengthOfLIS(nums)
            print(' and the LIS is ', res)


test(SolutionV3, False)
