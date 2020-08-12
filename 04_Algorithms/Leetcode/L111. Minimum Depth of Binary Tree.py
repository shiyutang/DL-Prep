# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            queue = [(root, 1)]
            while queue:
                node, level = queue.pop(0)
                children = (node.left, node.right)
                if not any(children):
                    return level

                for nei in children:
                    if nei:
                        queue.append((nei, level + 1))


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = ['']

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.minDepth(tree)
print(res)