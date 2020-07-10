from random import random


class Solution:
    def findRepeatNumber(self, nums) -> int:
        memoi = set()
        for i, num in enumerate(nums):
            if num in memoi:
                return num
            else:
                memoi.add(num)


sol = Solution()
print(sol.findRepeatNumber([2, 1, 3, 3]))
# print(sol.findRepeatNumber([]))
# print(sol.findRepeatNumber([2, 1, 3, 1, 4, 5]))
