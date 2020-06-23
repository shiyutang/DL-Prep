## this will print a BST in matrix


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 给定一个二叉树的头节点打印这个树
class PrintTree(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.height(root)
        matrix = [['' for n in range((2 ** h) - 1)] for m in range(h)]

        self.place(root, matrix, 0, (2 ** h) - 1, 0)
        for lists in matrix:
            print(lists)
        return matrix

    def height(self, node):
        return max(1 + self.height(node.left), 1 + self.height(node.right)) if node else 0

    def place(self, node, matrix, i, j, row):
        if node:
            col = (i + j) // 2
            matrix[row][col] = str(node.val)
            self.place(node.left, matrix, i, col, row + 1)
            self.place(node.right, matrix, col + 1, j, row + 1)


# from list to tree
from collections import deque

# 输入一个list，按照层次遍历的方式，建立一个树
def list2Tree(data):
    n = iter(data)
    tree = TreeNode(next(n))
    fringe = deque([tree])
    while True:
        head = fringe.popleft()
        try:
            tmp = next(n)
            if tmp is None:
                head.left = None
            else:
                head.left = TreeNode(tmp)
                fringe.append(head.left)
            tmp = next(n)
            if tmp is None:
                head.right = None
            else:
                head.right = TreeNode(tmp)
                fringe.append(head.right)
        except StopIteration:
            break
    return tree


data = [3, 5, 2, 1, 4, 6, 7, 8, 9, 0, 1, 2, 3, 4]
data = [5, 1, 4, None, None, 3, 6]
data = [17, 6, None, 5, 20, 3, 14, 20, 16, 9, 15, 10, 3, 17, None]
tree = list2Tree(data)

printT = PrintTree()
res = printT.printTree(tree)

# test

# from Debug_BST import list2Tree, PrintTree

# sol = Solution()
# data = [8, 6, 10, 5, 7, 9, 11]
#
# tree = list2Tree(data)
# printT = PrintTree()
# printT.printTree(tree)
#
# res = sol.Serialize(tree)
# print(res)