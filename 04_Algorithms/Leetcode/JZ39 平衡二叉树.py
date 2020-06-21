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
    def IsBalanced_Solution(self, pRoot):
        maxdepth, mindepth = -1, float('inf')

        def helper(node, depth, maxdepth, mindepth):
            if not node:
                return depth, maxdepth, mindepth
            else:
                leftdepth, maxdepth, mindepth = helper(node.left, depth + 1,maxdepth, mindepth)
                rightdepth, maxdepth, mindepth = helper(node.right, depth + 1,maxdepth, mindepth)
                mindepth = min(mindepth, min(leftdepth, rightdepth))
                maxdepth = max(maxdepth, max(leftdepth, rightdepth))
                # print(node, maxdepth, mindepth)
                return max(rightdepth, leftdepth), maxdepth, mindepth

        if not pRoot:
            return True
        else:
            dep, maxdepth, mindepth = helper(pRoot, 0, maxdepth, mindepth)
            return maxdepth - mindepth < 2


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = [5, 1, 7, None, None, 6, 8]
    data = [1, 2, 3, 4, 5, None, None, None, None, 6]

    tree = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree)

    res = sol.IsBalanced_Solution(tree)
    print('the res is', res)


test(Solution, True)
