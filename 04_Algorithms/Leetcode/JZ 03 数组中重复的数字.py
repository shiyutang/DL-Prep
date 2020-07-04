import random


class Solution:
    def findRepeatNumber(self, nums) -> int:
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0:
                if num == prev:
                    return num
                else:
                    prev = num
            else:
                prev = num


sol = Solution()
print(sol.findRepeatNumber([2, 1, 3, 3]))
print(sol.findRepeatNumber([]))
data = [random.randint(2, 100000) for _ in range(100000)]
print(sol.findRepeatNumber(data))
