# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            node = pHead
            Dummyhead = ListNode(0)
            prev = Dummyhead

            while node and node.next:
                if node.val == node.next.val:
                    before = node.next
                    node = node.next.next

                else:
                    prev.next = node
                    prev = node
                    before = node
                    node = node.next

            if not node or before.val != node.val:
                prev.next = node

        return Dummyhead.next