# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        def helper(node, depth):
            if not node:
                return depth
            else:
                ret = max(helper(node.right, depth + 1), helper(node.left, depth + 1))
            return ret

        if not pRoot:
            return 0
        else:
            return max(helper(pRoot.left, 1), helper(pRoot.right, 1))
