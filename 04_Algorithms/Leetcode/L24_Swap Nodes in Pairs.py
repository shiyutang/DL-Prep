# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            first = head
            second = first.next
            afternode = second.next
            
            head = second
            head.next = first
            first.next = afternode

            while afternode and afternode.next:
                prevnode = first
                first,second = afternode,afternode.next
                afternode = second.next

                prevnode.next = second
                second.next = first
                first.next = afternode
                
        return head
