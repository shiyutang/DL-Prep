class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 后序遍历，如果没有孩子，自己是0，就删除
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def traverse(node):
            if not node:
                return node
            node.left = traverse(node.left)
            node.right = traverse(node.right)
            if node.val == 0 and not node.left and not node.right:
                return None
            else:
                return node

        root = traverse(root)

        return root


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [1, 1, 0, 0, 0, 0, 1]
data = [0, 0, 0, 0, 0, 0, 0]
data = [1, 0, 0, 0, 0, 0, 0]
data = [1, 0, 1, 0, 1, 1, 0]
data = [1, 1, 0, 1, 1, 0, 1, 0]
data = [1, 0, 1, 0, 0, 0, 1]
# data = [1]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.pruneTree(tree)
print(res)
printT.printTree(res)
