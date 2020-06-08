class Solution:
    def canCompleteCircuit(self, gas, cost):
        playyard = [gas[i] - cost[i] for i in range(len(gas))]
        if sum(playyard) < 0:
            return -1
        startIdx = len(playyard)
        cnt = 0
        for i in range(len(playyard) - 1, -1, -1): # 从后往前，看哪些 index 积累下来能大于 0，其实和第二种方法相同，只是反向了
            if startIdx == len(playyard):
                if playyard[i] >= 0:
                    startIdx = i
                else:
                    continue
            else:
                cnt += playyard[i]
                if cnt > 0 and playyard[i] > 0:
                    startIdx = i

        return startIdx

# 另外一种解法是从头走到尾，当前面累计值小于 0 了，说明前面走不通的，所以清空累计值，从下一个开始！！
# 这种方法更加自然，符合想法：只要走不通就抛弃！

# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    params = [[[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
              [[2, 3, 4], [3, 4, 3]],
              [[5, 1, 10, 3, 1, 8, 3], [1, 5, 5, 5, 5, 5, 5]]]
    for param in params:
        a, b = param[0], param[1]
        res = sol.canCompleteCircuit(a, b)
        print(' and the start is ', res)

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
