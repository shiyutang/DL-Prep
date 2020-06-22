# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if exponent < 0:
            if base == 0:
                return
            else:
                base = 1 / base
                exponent = -exponent

        def fastpow(a, b):
            if b == 1:
                return a
            elif b == 0:
                return 1

            if b % 2 == 0:
                res = fastpow(a * a, b // 2)
            else:
                res = a * fastpow(a * a, b // 2)
            return res

        return fastpow(base, exponent)


sol = Solution()
print(sol.Power(2, -3))
print(sol.Power(2, 0))
print(sol.Power(0, 1))
