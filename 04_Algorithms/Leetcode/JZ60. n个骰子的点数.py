# 根据动态规划，不断把前面六个状态的结果加起来得到当前的结果除以总次数则得到了结果
class Solution:
    def twoSum(self, n: int) -> list:
        dp = [0 for i in range(6 * n)]
        dp[0:6] = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]

        for i in range(2, n + 1):
            for num in range(6 * i - 1, i - 2, -1):  # 同时需要更新的值是到i的前一位
                dp[num] = sum([dp[num - j] / 6 for j in range(1, 7) if num - j >= i - 2])  # 注意边界，不是数组的边界而是可以达到的最小

        return dp[n - 1:6 * n]


# [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 1, 3, 6, 10, 15, 21, 25, 27, 27, 25, 21, 15, 10, 6, 3, 1]

sol = Solution()
print(sol.twoSum(3))
