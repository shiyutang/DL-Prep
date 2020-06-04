class Solution:
    def maxProfit(self, prices):
        if prices == [] or len(prices) == 1:
            return 0
        diff = []
        for i in range(1,len(prices)):
            diff.append((prices[i]-prices[i-1]))
        print(diff)
        for i in range(len(diff)-1,0,-1):
            if diff[i]>0:
                diff[i-1] += diff[i]
        return max(max(diff),0)
sol = Solution()
# res = sol.maxProfit([7,1,5,3,6,4])
# print(res)
res = sol.maxProfit([7,6,4,3,1])
print(res)
