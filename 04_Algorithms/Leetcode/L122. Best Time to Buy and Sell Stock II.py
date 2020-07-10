class Solution:
    def maxProfit(self, prices: list) -> int:
        ret = 0
        for i in range(len(prices) - 1):
            ret = [ret, ret + prices[i + 1] - prices[i]][prices[i + 1] - prices[i] > 0]
        return ret


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 5, 4, 3, 2]))
print(sol.maxProfit([1, 2, 3, 4, 5, 6]))
print(sol.maxProfit([1, 3, 2, 6, 2, 4]))
