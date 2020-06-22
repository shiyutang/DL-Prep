# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        else:
            tmp1 = pHead1
            tmp2 = pHead2
            dummy = ListNode(0)
            pointer = dummy
            while tmp1 and tmp2:
                if tmp1.val < tmp2.val:
                    pointer.next = tmp1
                    tmp1 = tmp1.next
                else:
                    pointer.next = tmp2
                    tmp2 = tmp2.next
                pointer = pointer.next
            if tmp1:
                pointer.next = tmp1
            if tmp2:
                pointer.next = tmp2

            return dummy.next

