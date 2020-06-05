from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A) -> int:
        ALen = len(A)
        if ALen < 3:
            return 0

        intervalL = []
        for i in range(1, ALen):
            intervalL.append(A[i] - A[i - 1])

        cnt = [1]
        for i in range(1, len(intervalL)):
            if intervalL[i] != intervalL[i - 1]:
                if cnt[-1] < 2:
                    cnt.pop()
                cnt.append(1)
            else:
                cnt[-1] += 1

        res = 0
        for key in cnt:
            NLen = key + 1
            res += ((NLen - 1) * (NLen - 2)) // 2

        return res


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    A = [1, 2, 3, 4]
    A = [17, 16, 15, 14, 13, 10, 13, 10, 13, 13, 18, 23, 28, 12, 5, 13, 14, 14, 15]
    print(A, end=' ')
    res = sol.numberOfArithmeticSlices(A)
    print(' and res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)
            print(nums, end=' ')
            res = sol.numberOfArithmeticSlices(nums)
            print(' and res is ', res)


test(Solution, True)
