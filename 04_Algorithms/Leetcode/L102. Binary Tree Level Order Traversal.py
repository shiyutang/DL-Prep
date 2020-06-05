from .Debug_BST import TreeNode, PrintTree, list2Tree


# BFS with tag
class Solution:
    def levelOrder(self, root: TreeNode):
        self.res = []

        def BFSwithTag(Q):
            while Q:
                (node, level) = Q.pop(0)
                if level > len(self.res) - 1:
                    self.res.append([node.val])
                else:
                    self.res[level].append(node.val)
                if node.left is not None:
                    Q.append((node.left, level + 1))
                if node.right is not None:
                    Q.append((node.right, level + 1))

        if root is not None:
            queue = [(root, 0)]
            BFSwithTag(queue)
        return self.res





