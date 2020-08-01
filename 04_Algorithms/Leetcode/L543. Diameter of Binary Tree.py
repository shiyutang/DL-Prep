# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        if root:
            def helper(node):
                if not node:
                    return 0
                leftdepth = helper(node.left)
                rightdepth = helper(node.right)

                self.diameter = max(self.diameter, rightdepth + leftdepth)
                return max(rightdepth, leftdepth) + 1

            helper(root)

        return self.diameter


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, None, 6, 10, 5, 7, 9, None, 1, 1, 1, 1, None, 1, 1, 1, 11]
data = [None]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.diameterOfBinaryTree(tree)
print(res)
