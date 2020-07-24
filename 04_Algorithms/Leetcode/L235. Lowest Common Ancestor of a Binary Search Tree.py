# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 找到横跨在两个数值之间的元素就是LCA in BST
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        maxval, minval = max(p.val, q.val), min(p.val, q.val)
        if maxval >= root.val >= minval:
            return root
        elif maxval < root.val:
            root = root.left
        else:
            root = root.right

        return self.lowestCommonAncestor(root, p, q)


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.lowestCommonAncestor(tree, TreeNode(2), TreeNode(8))
print(res.val)
