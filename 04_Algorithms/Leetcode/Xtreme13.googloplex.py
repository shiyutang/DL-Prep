class Solution:
    def mod(self, b, p, m):
        res = 1
        while p:
            if p % 2:
                res = res * b % m
            b = b * b % m
            p = p >> 1
        return res

    def calculate(self, X, Y):
        modular = 10 ** Y
        X = X % (modular)

        minres = self.mod(X, 10**100, modular)
        res = minres
        for _ in range(86399):
            res = (res * X) % modular
            if res < minres:
                minres = res

        return minres


ncases = int(input())
sol = Solution()
for k in range(ncases):
    distance, wormhole = list(map(int, input().split(' ')))
    print(sol.calculate(distance, wormhole))
