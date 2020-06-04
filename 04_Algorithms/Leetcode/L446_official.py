class Solution(object):
    def numberOfArithmeticSlices(self, A):
        lookup = {}

        for i, a in enumerate(A):
            if a in lookup:
                lookup[a].append(i)
            else:
                lookup[a] = [i]

        dp = []
        for _ in range(len(A)):
            dp.append({})

        for k, num in enumerate(A):
            for i in range(0, k):
                diff = A[k] - A[i]
                X = A[i] - diff
                if X in lookup:
                    for index in lookup[X]:
                        if index < i:
                            dp[k][diff] = dp[k].get(diff, 0) + 1

                if diff in dp[i]:
                    dp[k][diff] = dp[k].get(diff, 0) + dp[i][diff]

        res = 0
        for x in dp:
            for k in x:
                res += x[k]

        return res
sol  = Solution()
sol.numberOfArithmeticSlices([2, 4, 6, 8, 10])