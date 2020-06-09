# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# tail connects to node index 0
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        else:
            nodeset = set()
            while head:
                if head in nodeset:
                    return head
                else:
                    nodeset.add(head)
                head = head.next

            return None
