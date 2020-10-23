# 1. 遍历map，碰到水格子对应father，
# 2. 遍历map，陆地格子对应到father，同时记录不同father 的邻居水格子
# 陆地格子连接的两个水格子距离为1,之后进行bfs
# 同一个水 father 为 0
import copy
from collections import defaultdict


class Solution:
    def __init__(self, map):
        self.map = map
        self.fathers = {}
        self.relation = defaultdict(set)  # water1: water2,water3

    def preprocessing(self):
        # step 1 & 2
        oneDis = defaultdict(set)

        for i in range(N):
            for j in range(M):
                if (i, j) not in self.fathers:
                    marked = {(i, j)}
                    q = [(i, j)]
                    father = (i, j)
                    if self.map[i][j] == '~':
                        while q:
                            node = q.pop(0)
                            self.fathers[node] = father
                            for nei in self.validneis(node):
                                if nei not in marked:
                                    if self.map[nei[0]][nei[1]] == '~':
                                        q.append(nei)
                                        marked.add(nei)
                    else:
                        while q:
                            node = q.pop(0)
                            self.fathers[node] = father
                            for nei in self.validneis(node):
                                if nei not in marked:
                                    if self.map[nei[0]][nei[1]] == 'O':
                                        q.append(nei)
                                        marked.add(nei)
                                    else:
                                        oneDis[father].add(nei)

        # print('sol.fathers', self.fathers)
        # print('oneDis', oneDis)

        for ele in oneDis:
            a = copy.deepcopy(oneDis[ele])
            for node in oneDis[ele]:
                if self.fathers[node] in a and node != self.fathers[node]:
                    a.remove(node)
            for node in a:
                self.relation[node] = self.relation[node].union(a)
        # print('self.relation', self.relation)

    def validneis(self, node):
        x, y = node
        neis = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1),
                (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
        return [nei for nei in neis if 0 <= nei[0] < N and 0 <= nei[1] < M]

    def solve(self, start, end):
        sfa, efa = self.fathers[start], self.fathers[end]
        # print('sfa,efa,self.relation', sfa, efa, self.relation)
        if sfa == efa:
            return 0
        else:
            if efa in self.relation[sfa]:
                return 1
            else:
                q = [(sfa, 0)]
                marked = {sfa}
                while q:
                    node, dis = q.pop(0)
                    ndis = dis + 1
                    for nei in self.relation[node]:
                        if nei == efa:
                            return ndis
                        if nei not in marked:
                            q.append((nei, ndis))
                            marked.add(nei)


N, M, Q = list(map(int, input().split(' ')))
rmap = []
for _ in range(N):
    rmap.append(list(input()))

sol = Solution(rmap)
sol.preprocessing()
for _ in range(Q):
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    print(sol.solve((x1 - 1, y1 - 1), (x2 - 1, y2 - 1)))


# 4 12 2
# OOOOO~~OOOOO
# O~~OO~OO~~~O
# OO~OO~~O~O~O
# OOOOOO~OOOOO
# 2 2 3 11
# 4 7 3 9

# # 1. 遍历map，碰到水格子对应father，
# # 2. 遍历map，陆地格子对应到father，同时记录不同father 的邻居水格子
# # 陆地格子连接的两个水格子距离为1，否则为2
# # 同一个水 father 为 0
# from collections import defaultdict
#
#
# class Solution:
#     def __init__(self, map):
#         self.map = map
#         self.fathers = {}
#         self.relation = defaultdict(set)  # water1: water2,water3
#
#     def preprocessing(self):
#         # step 1
#         for i in range(N):
#             for j in range(M):
#                 if self.map[i][j] == '~' and (i, j) not in self.fathers:
#                     marked = {(i, j)}
#                     q = [(i, j)]
#                     father = (i, j)
#                     while q:
#                         node = q.pop(0)
#                         self.fathers[node] = father
#                         for nei in self.validneis(node):
#                             if nei not in marked:
#                                 if self.map[nei[0]][nei[1]] == '~':
#                                     q.append(nei)
#                                 marked.add(nei)
#         # print('sol.fathers', self.fathers)
#
#         # step 2
#         oneDis = defaultdict(set)
#         for i in range(N):
#             for j in range(M):
#                 if self.map[i][j] == 'O' and (i, j) not in self.fathers:
#                     marked = {(i, j)}
#                     q = [(i, j)]
#                     father = (i, j)
#                     while q:
#                         node = q.pop(0)
#                         self.fathers[node] = father
#                         for nei in self.validneis(node):
#                             if nei not in marked:
#                                 if self.map[nei[0]][nei[1]] == 'O':
#                                     q.append(nei)
#                                 else:
#                                     oneDis[father].add(self.fathers[nei])
#                                 marked.add(nei)
#                         # print('node,self.relation,marked', node,self.relation,marked)
#
#         for ele in oneDis:
#             for node in oneDis[ele]:
#                 self.relation[node] = self.relation[node].union(oneDis[ele])
#                 # print(node, oneDis[ele], self.relation)
#         # print('oneDis', oneDis)
#
#     def validneis(self, node):
#         x, y = node
#         neis = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1),
#                 (x - 1, y - 1), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y + 1)]
#         return [nei for nei in neis if 0 <= nei[0] < N and 0 <= nei[1] < M]
#
#     def solve(self, start, end):
#         sfa, efa = self.fathers[start], self.fathers[end]
#         # print('sfa,efa,self.relation', sfa, efa, self.relation)
#         if sfa == efa:
#             return 0
#         else:
#             if efa in self.relation[sfa]:
#                 return 1
#             else:
#                 q = [(sfa, 0)]
#                 marked = {sfa}
#                 while q:
#                     node, dis = q.pop(0)
#                     ndis = dis + 1
#                     for nei in self.relation[node]:
#                         if nei == efa:
#                             return ndis
#                         if nei not in marked:
#                             q.append((nei, ndis))
#                             marked.add(nei)
#
#
# N, M, Q = list(map(int, input().split(' ')))
# rmap = []
# for _ in range(N):
#     rmap.append(list(input()))
#
# sol = Solution(rmap)
# sol.preprocessing()
# for _ in range(Q):
#     x1, y1, x2, y2 = list(map(int, input().split(' ')))
#     print(sol.solve((x1 - 1, y1 - 1), (x2 - 1, y2 - 1)))