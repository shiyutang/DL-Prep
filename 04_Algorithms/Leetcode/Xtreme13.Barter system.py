# ok *2 NZE*8,TLE*2，WA1
# ok *10,TLE*3 修改了representation 里面的
# 通过给的N对关系，建立图
# 通过图，BFS 找到目标物，计算乘积余998244353的结果
from collections import defaultdict
from fractions import Fraction


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def Inv(a, m):  # 这个扩展欧几里得算法求模逆
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m  # 逆元b


class Solution:
    def __init__(self):
        self.M = 998244353

    def solve(self):
        A, B = input().split(' ')
        if A == B:
            return 1
        if self.rep[A][0] != self.rep[B][0]:
            return -1
        return int((self.rep[B][1] * Inv(self.rep[A][1], self.M)) % self.M)

    def buildG(self):
        rM = defaultdict(list)
        for _ in range(N):
            A, B, W = input().split(' ')
            W = int(W)
            rM[A].append((B, W))
            rM[B].append((A, Fraction(1, W)))
        print(rM)

        rep = {}
        marked = set()
        for r in rM:
            if r in marked:
                continue
            q = [(r, 1)]
            marked.add(r)
            rep[r] = (r, 1)
            while q:
                node, val = q.pop(0)
                for nei in rM[node]:
                    if nei[0] not in marked:
                        if nei[1] < 1:
                            # 注意，如果nei[1] < 1 则相乘就是相除，需要用拓展欧几里得求逆元
                            tmp = (val * Inv(Fraction(1, nei[1]), self.M)) % self.M
                        else:
                            tmp = (val * nei[1]) % self.M
                        q.append((nei[0], tmp))
                        marked.add(nei[0])
                        rep[nei[0]] = (r, tmp)

        self.rep = rep
        print(self.rep)


N = int(input())
sol = Solution()
sol.buildG()
Q = int(input())
for _ in range(Q):
    print(sol.solve())
