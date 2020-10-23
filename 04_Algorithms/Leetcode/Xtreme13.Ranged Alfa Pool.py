class Solution:
    def __init__(self):
        self.memoi = [1]
        self.mod = 10 ** 9 + 7

    def NbrofGames(self, points):
        for i in range(1, points + 1):
            cumsum = 1
            res = 0
            while i >= cumsum:
                res = (res + self.memoi[i - cumsum]) % self.mod
                cumsum = 2 * cumsum + 1

            self.memoi.append(res)
        # print(self.memoi)

        return self.memoi[points]

    def calrange(self, points):
        if points == 0:
            return 1
        else:
            return (2 * sol.memoi[points]) % sol.mod


testcases = int(input())
sol = Solution()
sol.NbrofGames(10 ** 6)
for k in range(testcases):
    A, B = list(map(int, input().split(' ')))
    res = 0
    for i in range(A, B + 1):
        res += sol.calrange(i)
    print(res % sol.mod)
