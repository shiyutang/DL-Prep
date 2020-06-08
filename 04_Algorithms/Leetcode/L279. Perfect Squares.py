import math


class Solution:
    def numSquares(self, n: int) -> int:
        times = [i for i in range(n + 1)]

        def helper(n):
            candi = math.sqrt(n)
            if candi == int(candi):
                times[n] = 1
                return 1

            for i in range(1, int(candi) + 1):  # 对于使用每个 i^2 的基础上
                for j in range(i * 2, n + 1):
                    times[j] = min(times[j], 1 + times[j - i ** 2])

        helper(n)

        return times[n - 1]


class Solution:
    def numSquares(self, n: int) -> int:
        if math.ceil(n ** 0.5) == math.floor(n ** 0.5):
            return 1
        dp = [i for i in range(n + 1)]
        for i in range(1, math.ceil(n ** 0.5) + 1):
            sqi = i ** 2
            for j in range(sqi, n + 1):
                dp[j] = min(dp[j], 1 + dp[j - sqi])
        return dp[n]


class Solution:
    def numSquares(self, n: int) -> int:
        if int(n ** .5) ** 2 == n: return 1
        A = [i * i for i in range(1, int(n ** .5) + 1)]
        S = set(A)

        def sq2(n):
            for a in A:
                tmp = n - a
                if tmp < a: break
                if tmp in S: return True
            return False

        if sq2(n): return 2
        for a in A:
            if sq2(n - a): return 3
        return 4


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    params = [48, 12, 85, 3, 4, 28]
    for param in params:
        res = sol.numSquares(param)
        print(' and the res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)
            nums = list(set(nums))
            amount = random.randint(0, 100)
            print('the coinage are', nums)
            res = sol.coinChange(nums, amount)
            print(' and the minimum combinations for amount {} is {}'.format(amount, res))


test(Solution, False)
