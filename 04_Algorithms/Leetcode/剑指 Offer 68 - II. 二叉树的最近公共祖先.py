from Debug_BST import list2Tree, PrintTree, TreeNode


# 查看两边（包含自己）是否有p，q，如果分别有，则返回节点，否则，返回有什么
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        if not root:
            return None

        leftcontent = self.lowestCommonAncestor(root.left, p, q)
        rightcontent = self.lowestCommonAncestor(root.right, p, q)
        if isinstance(leftcontent, int) or isinstance(rightcontent, int):
            return leftcontent if isinstance(leftcontent, int) else isinstance(rightcontent, int)
        # print(rightcontent, leftcontent, root.val, self.find, self.res)
        if isinstance(leftcontent, TreeNode) and isinstance(rightcontent, TreeNode):
            return root.val
        elif isinstance(leftcontent, TreeNode) or isinstance(rightcontent, TreeNode):
            if root.val == p.val or root.val == q.val:
                return root.val
            else:
                return leftcontent if isinstance(leftcontent, TreeNode) else rightcontent
        else:
            if root.val == p.val or root.val == q.val:
                return root
            else:
                return None


sol = Solution()
data = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.lowestCommonAncestor(tree, TreeNode(5), TreeNode(4))
print(res)
