# BFS with tag, 每次得到结果之后反向~
class Solution:
    def Print(self, root):
        res = []

        def BFSwithTag(Q):
            while Q:
                (node, level) = Q.pop(0)
                if level > len(res) - 1:
                    res.append([node.val])
                    if level % 2 == 0 and level > 0:
                        res[-2].reverse()
                else:
                    res[level].append(node.val)
                if node.left is not None:
                    Q.append((node.left, level + 1))
                if node.right is not None:
                    Q.append((node.right, level + 1))
            if level % 2 == 1:
                res[-1].reverse()

        if root is not None:
            queue = [(root, 0)]
            BFSwithTag(queue)

        return res

from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 6, 10, 5, 7, 9, 11,1,2,1,3,1,4,1,5,2,3,1,3]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.zigzagLevelOrder(tree)
print(res)