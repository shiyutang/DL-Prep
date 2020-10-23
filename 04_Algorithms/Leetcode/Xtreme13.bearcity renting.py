from collections import defaultdict


class MST:
    def __init__(self):
        self.node = dict()
        self.rank = dict()
        self.nodeEdge = defaultdict(set)

    def make_set(self, point):
        self.node[point] = point  # connnect to itself
        self.rank[point] = 0  # the size of the father

    def find(self, point):
        if self.node[point] != point:  # not connect to itself
            self.node[point] = self.find(self.node[point])  # connect to it father
        return self.node[point]

    def merge(self, point1, point2):
        root1 = self.find(point1)
        root2 = self.find(point2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.node[root2] = root1
            else:
                self.node[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

    def Kruskal(self, graph):
        for vertice in graph['vertices']:
            self.make_set(vertice)

        mst = set()
        edges = graph['edges']
        edges.sort()  # sort edge
        self.edges = edges
        for edge in edges:
            weight, v1, v2 = edge
            if self.find(v1) != self.find(v2):  # as long as the lighter edge connect to different party, merge them
                self.merge(v1, v2)
                mst.add(edge)
        return mst

    def replacable(self, node2):
        return len(self.nodeEdge[node2]) > 1

    def removeedges(self, graph):
        MSTedgeset = self.Kruskal(graph)  # {(1, '1', '3'), (2, '2', '4'), (2, '2', '5'), (2, '1', '2'), (2, '1', '6')}
        for e in MSTedgeset:
            w, node1, node2 = e
            self.nodeEdge[node2].add((node1, w))
            self.nodeEdge[node1].add((node2, w))
        # print(MSTedgeset)

        replaced = set()  # (v1,v2,weight)
        # base on current MST
        for edge in self.edges:
            if edge in MSTedgeset:  # for all other edge
                continue
            else:
                v12weight, v1, v2 = edge  # current edge
                for MEdge in MSTedgeset:
                    # all other edge v1 v2 connect: if able to replace
                    # print(edge, MEdge)
                    v34weight, v3, v4 = MEdge
                    if v1 == v4 and (v3, v34weight) in self.nodeEdge[v1]:
                        if v3 != v2 and v12weight == v34weight and (v1, v3) not in replaced and (v3, v1) not in replaced:
                            if self.replacable(v3):
                                replaced.add((v1, v3))
                    elif v1 == v3 and (v4,v34weight) in self.nodeEdge[v1]:
                        if v4 != v2 and v12weight == v34weight and (v1, v4) not in replaced and (v4, v1) not in replaced:
                            if self.replacable(v4):
                                replaced.add((v1, v4))
                    elif v2 == v4 and (v3,v34weight) in self.nodeEdge[v2]:
                        if v3 != v1 and v12weight == v34weight and (v2, v3) not in replaced and (v3, v2) not in replaced:
                            if self.replacable(v3):
                                replaced.add((v1, v3))
                    elif v2 == v3 and (v4,v34weight) in self.nodeEdge[v2]:
                        if v4 != v1 and v12weight == v34weight and (v2, v4) not in replaced and (v4, v2) not in replaced:
                            if self.replacable(v4):
                                replaced.add((v2, v4))
                    else:
                        if MEdge[0] == v12weight:
                            if self.replacable(MEdge[1]) and self.replacable(MEdge[2]):
                                replaced.add((MEdge[1], MEdge[2]))
        # print(replaced)

        return len(MSTedgeset) - len(replaced)


nodes, edges = list(map(int, input().split(' ')))
graph = {'vertices': ['{}'.format(i) for i in range(1, nodes + 1)],
         'edges': []}

for _ in range(edges):
    v1, v2, w = input().split(' ')
    graph['edges'].append((int(w), v1, v2))

sol = MST()
print(sol.removeedges(graph))

# 6 9
# 1 2 2
# 1 3 1
# 1 6 2
# 2 4 2
# 2 5 2
# 4 3 2
# 3 5 2
# 4 5 4
# 5 6 4
