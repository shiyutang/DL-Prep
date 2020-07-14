# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    def cmp(self, s, t):
        if (not s and t) or (not t and s):
            return False
        elif not s and not t:
            return True
        else:
            if s.val != t.val:
                return False
            else:
                return self.cmp(s.right, t.right) and self.cmp(s.left, t.left)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False

        res1 = self.isSubtree(s.left, t)
        res2 = self.isSubtree(s.right, t)

        return self.cmp(s, t) or res1 or res2


# test
def test(method, random_samples=False):
    sol = method()
    data = [5, 1, 7, None, None, 6, 8]

    tree1 = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree1)

    # data = [7, 6, 8]
    data = [8]

    tree2 = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree2)

    res = sol.isSubtree(tree1, tree2)
    print('the res is', res)


test(Solution, False)
