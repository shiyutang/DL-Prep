# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# method:使用层次遍历的方式序列化（层次遍历就是用队列的方式，一个个加入）
# 之后因为是层次遍历，将得到的节点一个个接到可以接的节点上
class Solution:
    def Serialize(self, root):
        if not root:
            return '!'
        else:
            res = []
            queue = [root]
            while queue:
                node = queue.pop(0)
                if node is None:
                    res.append('#')
                else:
                    res.append(node.val)
                    queue.extend([node.left, node.right])
            res.append('!')
            return res

    def Deserialize(self, s):
        s = s[:-1]
        if not s:
            return
        else:
            def toNode(val):
                if val is '#':
                    return None
                else:
                    return TreeNode(val)

            queue = s[1:]
            root = TreeNode(s[0])
            roots = [root]
            while queue:
                left, right = queue.pop(0), queue.pop(0)
                ancester = roots.pop(0)
                ancester.left = toNode(left)
                ancester.right = toNode(right)
                if ancester.left:
                    roots.append(ancester.left)
                if ancester.right:
                    roots.append(ancester.right)
            return root


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 6, 10, 5, 7, 9, 11]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.Serialize(tree)
print(res)
res = sol.Deserialize(res)
printT.printTree(res)
