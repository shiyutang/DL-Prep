# Given two BSTs, merge to one BST and balance it.

class Treenode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


class task:
    def __init__(self):
        self.tree1 = []
        self.tree2 = []

    def merge(self,tree1, tree2):
        self.tree1 = self.inorder(tree1)
        self.tree2 = self.inorder(tree2)
        tree = self.mergesort(self.tree1, self.tree2)

        return self.deserialize(tree)

    def inorder(self, root):
        ret = []
        if not root:
            return ret
        else:
            def helper(node):
                if not node:
                    return
                helper(node.left)
                ret.append(node.val)
                helper(node.right)

            helper(root)
            return ret

    def mergesort(self,a, b):
        ret = []
        while a and b:
            if a[0] > b[0]:
                ret.append(a.pop(0))
            else:
                ret.append(b.pop(0))
        if a:
            ret.extend(a)
        if b:
            ret.extend(b)
        return ret

    def deserialize(self, tree):
        if not tree:
            return None

        low = 0
        high = len(tree) - 1
        mid = (low + high) // 2

        root = Treenode(tree[mid])
        root.left = self.deserialize(tree[:mid])
        root.right = self.deserialize(tree[mid + 1:])

        return root


#         0
#     1         1
#   2   3     3   2
#  4 5 6  7

class Task:
    def traverse(root):
        if not root:
            return True
        else:
            queue = [(root, 0)]
            levelst = []
            depth = -1
            flag = True
            while queue:
                node, level = queue.pop(0)
                width = 2 ** level
                for nei in (node.left, node.right):
                    queue.append((nei, level + 1))

                if depth != level:
                    levelst = [node]
                    depth = level
                elif len(levelst) <= width // 2:
                    levelst.append(node)
                else:
                    nodepop = levelst.pop(-1)
                    if nodepop is None:
                        if node is not None:
                            flag = False
                    else:
                        if not node or levelst.pop(-1).val != node.val:
                            flag = False
                            break

            return flag




