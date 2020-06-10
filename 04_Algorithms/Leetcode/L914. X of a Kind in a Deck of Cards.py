from collections import Counter
from math import gcd
# 使用reduce 化简程序
class Solution:
    def hasGroupsSizeX(self, deck: list) -> bool:
        record = Counter(deck)
        init = -1
        for ele in set(record.values()):
            init = [init, ele][init == -1]
            if gcd(ele, init) < 2:
                return False

        return True


from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: list) -> bool:
        count = Counter(deck).values()
        return reduce(gcd, count) > 1


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    # data = [1, 2, 3, 4, 4, 3, 2, 1]
    # data = [1, 2, 3, 3, 3, 3, 2, 1]
    data = [1, 2, 3, 2, 4, 3, 2, 1]
    # data = [1, 2, 3, 1, 2, 3, 2, 1]
    # data = [1, 2, 2, 2, 2, 2, 2, 1]
    # data = [1, 1]
    # data = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
    res = sol.hasGroupsSizeX(data)
    print(res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 3)
                nums.append(num1)
            print('the nums are', nums)
            res = sol.hasGroupsSizeX(data)
            print(res)


test(Solution, True)
