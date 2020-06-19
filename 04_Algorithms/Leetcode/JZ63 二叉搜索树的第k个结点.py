# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 中序遍历到第k个结点返回
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):

        def helper(node):
            if not node:
                return
            helper(node.left)
            curr_idx = 0
            global curr_idx
            curr_idx += 1
            if curr_idx == k:
                return node.val
            helper(node.right)

        if pRoot and k > 0:
            return helper(pRoot)
        else:
            return
