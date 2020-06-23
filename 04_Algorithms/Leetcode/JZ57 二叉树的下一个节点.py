# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# 根节点的下一个为右节点的孩子中中最左的节点，否则就是自己
# 右节点的下一个为右拐的第一个根节点
# 左节点的下一个为根节点
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        else:
            # 有右节点就当作根节点
            if pNode.right:    # 注意索引节点的时候要保证该节点有效
                tmp = pNode.right
                while tmp.left:
                    tmp = tmp.left
                return tmp
            else:
                # 没有右节点可以是左/右孩子
                # 没有根节点是根
                if not pNode.next:
                    return
                # 有根节点的左节点
                elif pNode.next.left == pNode:
                    return pNode.next
                # 有根节点的右孩子
                else:
                    tmp = pNode
                    while tmp == tmp.next.right:
                        tmp = tmp.next
                        if tmp.next is None:  # 没有下一个节点的右节点就是一直翻上去最后翻到根
                            return
                    return tmp.next


