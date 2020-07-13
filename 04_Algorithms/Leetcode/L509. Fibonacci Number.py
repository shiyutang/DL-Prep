class Solution:
    def fib(self, N: int):
        if N < 0:
            return
        elif N < 2:
            return N
        a, b = 0, 1
        for i in range(2, N + 1):
            c = a + b
            a, b = b, c

        return c
