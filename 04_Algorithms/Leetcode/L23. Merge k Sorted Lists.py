# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 每次都把最小的数放入优先队列，并索引出最小值放入链表
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        q = PriorityQueue()
        dummy = ListNode(0)
        pre = dummy
        for i, node in enumerate(lists):
            # print(node.val, node, q)
            if node:
                q.put((node.val, i, node))  # listnode 不能比较，所以需要在val相等时，额外增加一个比较

        while q.qsize():
            tag, node = q.get()[1:]
            pre.next = node
            pre = node
            # print(node.val)

            if node.next:
                tmp = node.next
                q.put((tmp.val, tag, tmp))
        return dummy.next


from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

# head1 = stringToListNode([1, 4, 5])
# head2 = stringToListNode([1, 3, 4])
# head3 = stringToListNode([2, 6])
head3 = stringToListNode([])
# prettyPrintLinkedList(head1)
sol = Solution()
prettyPrintLinkedList(sol.mergeKLists([head3]))
