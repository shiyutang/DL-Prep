# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 法 2 严格O（N）：快慢指针 快指针先往前走k步，注意判断边界，然后快慢一起走，当快指针为none的时候，慢指针走到了倒数第k个节点
class Solution:
    def FindKthToTail(self, head, k):
        if not head:
            return
        else:
            cnt = 0
            tmp = head
            while tmp:
                cnt += 1
                tmp = tmp.next
            if cnt < k:
                return
            else:
                idx = cnt - k
                cnt = 0
                tmp = head
                while cnt < idx:
                    tmp = tmp.next
                    cnt += 1
                return tmp
