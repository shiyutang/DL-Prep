# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        else:
            res = [root.val]
            queue = [root]
            while queue:
                node = queue.pop(0)
                # print(node.val)
                for nei in (node.left, node.right):
                    if nei:
                        queue.append(nei)
                        res.append(nei.val)
        return res

def test(method):
    # test settings

    sol = method()
    data = [10, 5, 12, 4, 7]
    data = [10,6,14,4,8,12,1]

    tree = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree)

    res = sol.PrintFromTopToBottom(tree)
    print(res)


test(Solution)