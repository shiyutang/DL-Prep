# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        else:
            def helper(node, prev):
                if not node:
                    return prev
                prev = helper(node.left, prev)

                prev.right = node
                if prev != dummyroot:
                    node.left = prev

                prev = helper(node.right, node)

                return prev

            dummyroot = TreeNode(0)
            _ = helper(pRootOfTree, dummyroot)
            return dummyroot.right

