# 1. 建树：
# 2. 给定节点填充数值，保存节点id和数值
# 3. 不断向上累计，并对每个节点判断是否为 LCA，对于 LCA 减去给定数值，并去除结果
# 记录路程中最大值并返回

class TreeNode:
    def __init__(self,id):
        self.id = id
        self.val = set()  # (id)
        self.depth = None
        self.parent: TreeNode
        self.parent = None
        self.cumsum = 0


class Solution:
    def __init__(self):
        self.root = None

    def solve(self):
        self.buildTree()
        weight = {}
        for i in range(M):
            s, e, w = list(map(int, input().split(' ')))
            weight[i] = w
            self.prev[s].val.add(i)
            self.prev[e].val.add(i)
        Nodes = list(self.prev.values())
        Nodes.sort(key=lambda x: x.depth)
        idx = len(Nodes) - 1
        maxval = 0
        for d in range(Nodes[-1].depth, 0, -1):
            while Nodes[idx].depth == d and idx >= 0:
                # current sum
                v = 0
                for ele in Nodes[idx].val:
                    v += weight[ele]
                Nodes[idx].cumsum += v

                maxval = max(maxval, v)

                # add value to parent
                tmp = Nodes[idx].parent.val.intersection(Nodes[idx].val)
                if len(tmp) != 0:
                    for ele in tmp:
                        v -= weight[ele]  # remove redundent value
                        if Nodes[idx].parent != self.root:
                            Nodes[idx].parent.parent.cumsum -= weight[ele]
                Nodes[idx].parent.cumsum += v

                idx -= 1

        return maxval

    def buildTree(self):
        self.prev = dict()
        for i in range(N - 1):
            u, v = list(map(int, input().split(' ')))
            if i == 0:
                vNode = TreeNode(v)
                self.root = TreeNode(u)
                vNode.parent = self.root
                self.prev[u] = self.root
                self.prev[v] = vNode
                self.root.depth = 1
                vNode.depth = 2
            else:
                if v not in self.prev:
                    vNode = TreeNode(v)
                    self.prev[v] = vNode
                    vNode.parent = self.prev[u]
                    vNode.depth = vNode.parent.depth + 1
                elif u not in self.prev:
                    uNode = TreeNode(u)
                    self.prev[u] = uNode
                    uNode.parent = self.prev[v]
                    uNode.depth = uNode.parent.depth + 1

        for ele in self.prev:
            print(ele, self.prev[ele].parent.id)


N, M = list(map(int, input().split(' ')))
sol = Solution()
print(sol.solve())
