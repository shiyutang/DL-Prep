# dp[i][W] 能否取到W等于sum(nums)/2
class Solution:
    def canPartition(self, nums) -> bool:
        pvalset = set()
        target = sum(nums) / 2
        for num in nums:
            if pvalset:
                tmp = set()
                for ele in pvalset:
                    tmp.add(num + ele)
                    if abs(num + ele - target) < 1e-4:
                        # print(num + ele, target)
                        return True
                pvalset = pvalset.union(tmp)
            pvalset.add(num)
            if num == target:
                return True
        return False


sol = Solution()
# print(sol.canPartition([1, 5, 5, 11]))
# print(sol.canPartition([1, 2, 3, 5]))
print(sol.canPartition([1, 1]))
