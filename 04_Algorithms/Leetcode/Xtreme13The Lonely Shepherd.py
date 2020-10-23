# 计算所有和已知的边之差一条边的节点的剩下那条边的比例

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.nei = []
        self.subtreeNodes = 0
        self.par = None


class Solution:
    def __init__(self):
        self.found = False
        self.theEdge = (None, None)

    def UpdateEdgeWeight(self, node: TreeNode):
        ans = 1
        for neinode in node.nei:
            if neinode == node.par:
                continue
            else:
                neinode.par = node
                ans += self.UpdateEdgeWeight(neinode)

        if ans == K:
            self.found = True
            self.theEdge = (node, node.par)
        elif ans == N - K:
            self.found = True
            self.theEdge = (node.par, node)

        return ans

    def SubtreeContent(self, root, otherRoot):
        ret = set()
        stack = [root]
        while stack:
            node = stack.pop(-1)
            ret.add(node.val)
            for nei in node.nei:
                if nei != otherRoot and nei.val not in ret and nei:
                    stack.append(nei)

        return ret


N, K = list(map(int, input().split(' ')))
TreeNodeDict = {i: TreeNode(i) for i in range(1,N+1)}
for i in range(N - 1):
    val1, val2 = list(map(int, input().split(' ')))
    TreeNodeDict[val1].nei.append(TreeNodeDict[val2])
    TreeNodeDict[val2].nei.append(TreeNodeDict[val1])

sol = Solution()
sol.UpdateEdgeWeight(TreeNodeDict[1])
if not sol.found:
    print(-1)
else:
    thisside, otherside = sol.theEdge
    content = sol.SubtreeContent(thisside, otherside)
    for i in content:
        print('flip',str(i))
    print('cut', sol.theEdge[0].val, sol.theEdge[1].val)
