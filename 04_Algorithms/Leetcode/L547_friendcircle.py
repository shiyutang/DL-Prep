# find number of friend circles
# 1. read right upper part of matrix and add connectivity in graph
# 2. find how many 'representative' here is and output
from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)  # record graph and its connection
        self.parent = [[-1] for j in range(vertices)]

    def addEdge(self, x, xconnect):
        self.graph[x].append(xconnect)

    def find(self, x):
        if self.graph[x] == [x] or self.graph[x] == []:
            return x
        else:
            for i in range(len(self.graph[x])):
                self.graph[x] = [self.find(self.graph[x][i])]
            return self.graph[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.graph[int(xroot)].append(yroot)

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        graph = Graph(len(M))
        for i in range(0,len(M)):
            for j in range(i+1, len(M)):
                if M[i][j] == 1:
                    graph.addEdge(i,j)
