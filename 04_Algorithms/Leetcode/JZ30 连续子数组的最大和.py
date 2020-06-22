# -*- coding:utf-8 -*-
# 时间复杂度 O(N) 空间复杂度 O(1)
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if not array:
            return
        p1, p2 = -1, -1
        maxval = -float('inf')
        for idx, num in enumerate(array):
            if p1 < 0 and p2 < 0:
                if num > 0:
                    p1, p2 = idx, idx
                sum = num
            elif p1 >= 0 and p2 >= 0:
                sum += num
                if sum > 0:
                    p2 += 1
                else:
                    p1 = p2 + 1
                    p2 = p2 + 1
                    sum = 0
            maxval = max(maxval, sum)
            # print(idx, p1, p2, sum, maxval)
        return maxval

# 也可以使用动态规划，记录某个 idx 之前的最优情况，看加上当前元素是否还是最优


sol = Solution()
print(sol.FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
print(sol.FindGreatestSumOfSubArray([-3, -2, -1, -15]))
print(sol.FindGreatestSumOfSubArray([-3, -2, -1, -15, 1]))
