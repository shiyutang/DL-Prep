class Solution:
    def coinChange(self, coins, amount) -> int:
        self.D = {}
        for coinage in coins:
            self.D[coinage] = 1

        return self.changeways(coins, amount)

    def changeways(self, coins, amount):
        if amount < 0:
            return -1
        elif amount == 0:
            return 0

        if amount in self.D:
            return self.D[amount]

        ways = 1e100
        for coinage in coins:
            res = self.changeways(coins, amount - coinage)
            if res is not -1:
                ways = min(ways, res+1)

        self.D[amount] = ways

        return [self.D[amount], -1][self.D[amount] == 1e100]


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    coins, amount = [1, 2, 5], 11
    print(coins, end=' ')
    res = sol.coinChange(coins, amount)
    print(' and the minimum coinchange is ', res)

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


test(Solution, True)
