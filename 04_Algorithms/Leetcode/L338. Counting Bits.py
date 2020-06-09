import math


class Solution:
    def countBits(self, num: int):
        dp = {0: 0}
        res = [0]

        def helper(num):
            for i in range(1, num+1):
                tmp = i - 2**int(math.log2(i))
                print('i, tmp', i, tmp)
                res.append(dp[tmp] + 1)
                dp[i] = dp[tmp] + 1
                print("res, dp", res, dp)

        helper(num)
        return res

# 没看懂 🤦‍
class Solution:
    def countBits(self, num: int):
        r = [0]
        for _ in range(int(math.log2(num + 1))):
            r += [1 + e for e in r]
            print(r)
        r += [1 + e for e in r[:num - len(r) + 1]]
        print(r)
        return r

# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    coins = 5
    print(coins, end=' ')
    res = sol.countBits(coins)
    print(' and the res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            coins = random.randint(1, 40)
            print(coins, end=' ')
            res = sol.countBits(coins)
            print(' and the res is ', res)


test(Solution, False)