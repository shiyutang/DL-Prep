# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 也可以在后序遍历中对根进行操作，这里使用层次遍历的方式，后序遍历同理
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return root
        else:
            queue = [root]
            while queue:
                node = queue.pop()
                for nei in (node.left,node.right):
                    if nei:
                        queue.append(nei)
                node.left, node.right =node.right, node.left
            return root


