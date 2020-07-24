# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 分别找到两个节点，然后在路径中找到一个重复元素
# 自底向上：后序遍历，如果根节点等于其中一个，并左右节点等于另一个，或者左右节点分别等于一个，则找到LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if not root:
            return False
        leftres = self.lowestCommonAncestor(root.left, p, q)
        rightres = self.lowestCommonAncestor(root.right, p, q)
        if isinstance(leftres, TreeNode):  # 左子树已全部找到
            return leftres
        elif isinstance(rightres, TreeNode):  # 右子树已全部找到
            return rightres
        elif leftres or rightres:   # 有1/2个找到
            if root.val == p.val or root.val == q.val or (leftres and rightres):
                return root
            else:
                return True
        else:                      # 子树均没有找到
            if root.val == p.val or root.val == q.val:  # 根找到一个
                return True
            else:
                return False


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.lowestCommonAncestor(tree, TreeNode(5), TreeNode(2))
print(res.val)
