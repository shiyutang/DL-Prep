# 40 TLE*4 nze*2 OK*4

import math
from functools import reduce


def fast_pow(under, exp):
    if under == 0:
        return 0
    elif under == 1:
        return 1
    else:
        if exp == 1:
            return under
        elif exp == 0:
            return 1
        elif exp % 2 == 1:
            res = under * fast_pow(under, (exp - 1) / 2) ** 2
        else:
            res = fast_pow(under, exp / 2) ** 2
        return res % (10 ** 9 + 7)


def comb(n, m):
    if m == 0 or n == 0:
        return 1
    tmp = reduce(lambda x, y: x * y, [i for i in range(n - m + 1, n + 1)])
    return tmp // math.factorial(m)


N = int(input())
for _ in range(N):
    a, b, c = list(map(int, input().split(' ')))
    if a == 1:
        print(1)
    else:
        print(fast_pow(a, comb(b, c)))
