# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# noinspection PyUnboundLocalVariable
# 只需要根据前/后序遍历找到根节点，然后利用根节点将中序遍历分割，再一次递归地传入就可以
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        def helper(preOrder, inOrder):
            if not preOrder or not inOrder:
                return
            elif len(preOrder) == 1:
                return TreeNode(preOrder[0])
            else:
                node = TreeNode(preOrder[0])
                for idx, num in enumerate(inOrder):
                    if preOrder[0] == num:
                        bp = idx
                        break
                node.left = helper(preOrder[1:bp + 1], inOrder[:bp])
                node.right = helper(preOrder[bp + 1:], inOrder[bp + 1:])
                return node

        root = helper(pre, tin)
        return root
