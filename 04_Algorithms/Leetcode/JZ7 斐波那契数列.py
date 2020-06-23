# -*- coding:utf-8 -*-
# 仅仅利用前面两个数，因此迭代地求就可以
class Solution:
    def Fibonacci(self, n):
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            a, b = 0, 1
            for i in range(2, n + 1):  # 循环要到n+1，不然走不到n！！！
                res = a + b
                a, b = b, res
            return res


sol = Solution()
print(sol.Fibonacci(2))
