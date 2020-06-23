# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# queue with Tag
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        else:
            ret = []
            queue = [(pRoot, 0)]
            while queue:
                node, level = queue.pop(0)
                if len(ret)<level+1:
                    ret.append([node.val])
                else:
                    ret[level].append(node.val)

                for nei in (node.left, node.right):
                    if nei is not None:
                        queue.append((nei, level + 1))
            return ret

from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 6, 10, 5, 7, 9, 11]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.Print(tree)
print(res)