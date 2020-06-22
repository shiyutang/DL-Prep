# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        else:
            dummyroot = RandomListNode(0)
            memoi = {}
            while pHead:
                if not dummyroot.next:
                    newpointer = RandomListNode(pHead.label)
                    memoi[newpointer] = pHead
                    if pHead.random not in memoi.values():
                        tmp = RandomListNode(pHead.random.label)
                        newpointer.random = tmp
                        memoi[tmp] = pHead.random
                    dummyroot.next = newpointer
                else:
                    pass


