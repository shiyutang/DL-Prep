# 中序遍历和对应右根左相同, 注意不要添加叶子节点的所有子节点，不然容易出现不对称的树也对称（见示例2）
# 输入为二叉树
class Solution:
    def isSymmetrical(self, pRoot):
        res1 = []
        res2 = []

        def inorder(node):
            if not node:
                res1.append(None)
            elif not node.left and not node.right:
                res1.append(node.val)
            else:
                inorder(node.left)
                res1.append(node.val)
                inorder(node.right)

        def rightinorder(node):
            if not node:
                res2.append(None)
            elif not node.left and not node.right:
                res2.append(node.val)
            else:
                rightinorder(node.right)
                res2.append(node.val)
                rightinorder(node.left)

        if not pRoot:
            return True
        else:
            inorder(pRoot)
            rightinorder(pRoot)
            print(res1, res2)
            return res1 == res2


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 5, 6, 5, 7, 7, 5]
data = [5, 5, 5, 5, None, None, 5, 5, None, 5]  #(示例2)

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.isSymmetrical(tree)
print(res)
