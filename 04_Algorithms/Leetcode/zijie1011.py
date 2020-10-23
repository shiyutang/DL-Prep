import copy
import math


class Solution:
    def __init__(self):
        self.memoi = [[{} for __ in range(M + 1)] for _ in range(N)]
        self.factorial = []

    def getS(self, Array):
        Array.sort()
        self.factorial = [math.factorial(Array[0])]
        for i in range(1, len(Array)):
            res = self.factorial[-1]
            for i in range(Array[i - 1] + 1, Array[i] + 1):
                res *= i
            self.factorial.append(res)

        self.memoi[0][M][0] = 1
        self.memoi[0][M][Array[0]] = 1
        self.memoi[0][M - 1][self.factorial[0]] = 1

        for i in range(1, len(Array)):
            # choose, not choose, factorial and not
            for j in range(min(M + 1, i + 2)):
                self.memoi[i][M - j] = copy.deepcopy(self.memoi[i - 1][M - j])  # not choose
                for ele in self.memoi[i - 1][M - j]:
                    # choose no fact
                    if ele + Array[i] <= S:
                        if ele + Array[i] in self.memoi[i][M - j]:
                            self.memoi[i][M - j][ele + Array[i]] += 1
                        else:
                            self.memoi[i][M - j][ele + Array[i]] = self.memoi[i-1][M-j][ele]

                if j > 0:
                    for ele in self.memoi[i - 1][M - j + 1]:
                        # choose fact
                        if ele + self.factorial[i] <= S:
                            if ele + self.factorial[i] in self.memoi[i][M - j]:
                                self.memoi[i][M - j][ele + self.factorial[i]] += 1
                            else:
                                self.memoi[i][M - j][ele + self.factorial[i]] = self.memoi[i-1][M-j+1][ele]
                # print(self.memoi)

        cnt = 0
        for i in range(M + 1):
            for ele in self.memoi[N - 1][M - i]:
                if ele == S:
                    cnt += self.memoi[N-1][M-i][ele]
        return cnt


N, M, S = list(map(int, input().split(' ')))
Array = list(map(int, input().split(' ')))
sol = Solution()
print(sol.getS(Array))

# 4 2 6
# 1 2 3 4
