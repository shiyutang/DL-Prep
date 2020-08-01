# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        pre = dummy
        h, t = head, head

        def reverse(subhead, tail):
            if subhead == tail:
                return subhead,tail
            current = subhead
            nextnode = subhead.next
            while nextnode != tail:
                nextnext = nextnode.next
                nextnode.next = current
                current = nextnode
                nextnode = nextnext
            nextnode.next = current
            return tail, subhead

        while t:
            cnt = 1
            while t and cnt < k:
                t = t.next
                cnt += 1

            if t:
                nxt = t.next

                h, t = reverse(h, t)

                # connect pre and nxt
                pre.next = h
                t.next = nxt
                # prepare for next round
                pre = t
                h, t = nxt, nxt

        return dummy.next


sol = Solution()
from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

# head = stringToListNode([0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11])
# prettyPrintLinkedList(head)
# prettyPrintLinkedList(sol.reverseKGroup(head, 3))
head = stringToListNode([1, 2, 3, 4, 5])
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.reverseKGroup(head, -1))

# print(sol.reverseKGroup())
