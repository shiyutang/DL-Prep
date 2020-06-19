# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        memoi = {2: 1, 3: 2}

        def helper(number):
            result = number
            if number in memoi:
                return max(result, memoi[number])

            for i in range(2, number - 1):
                result = max(result, helper(number - i) * i)

            memoi[number] = result

            return result

        res = number - 1
        for i in range(2, number - 1):
            res = max(res, helper(number - i) * i)
        return res


def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = 8
    res = sol.cutRope(data)
    print(res)

    if random_samples:
        import random
        for _ in range(times):
            data = random.randint(2, 20)
            print(data)
            res = sol.cutRope(data)
            print(res)


test(Solution, True)