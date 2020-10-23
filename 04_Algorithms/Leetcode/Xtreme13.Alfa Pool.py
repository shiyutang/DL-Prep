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


testcases = int(input())
sol = Solution()
sol.NbrofGames(10**5)
for k in range(testcases):
    points = int(input())
    if points == 0:
        print(1)
    else:
        print((2 * sol.memoi[points]) % sol.mod)

sol = Solution()
print(sol.NbrofGames(5))
sol = Solution()
print(sol.NbrofGames(7))
