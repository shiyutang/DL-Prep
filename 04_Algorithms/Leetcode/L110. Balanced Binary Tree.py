# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历，并统计深度，如果左右深度只差大于1 则不是平衡二叉树
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def traverse(node):
            if not node:
                return 0
            leftdepth = traverse(node.left)
            rightdepth = traverse(node.right)
            if abs(leftdepth - rightdepth) > 1 or leftdepth == -1 or rightdepth == -1:
                return -1

            return max(leftdepth, rightdepth) + 1

        return [True, False][traverse(root) == -1]


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 1, 10, 5, None, None, 11]
data = [8, 10, 1, 1, None, None, 8, None, 19]
data = [1, 2, 2, 3, 3, None, None, 4, 4]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.isBalanced(tree)
print(res)
