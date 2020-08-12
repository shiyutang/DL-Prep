# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. 全部装入栈中，依次取首尾元素就可
# 2. 将链表从中间分成两个链表,倒序后面的链表,依次按奇偶插入链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        deque = []
        pointer = head
        while pointer:
            deque.append(pointer)
            pointer = pointer.next

        p = deque.pop(0)
        while deque:
            p.next = deque.pop(-1)
            p = p.next

            if deque:
                p.next = deque.pop(0)
                p = p.next

        p.next = None
        prettyPrintLinkedList(head)


from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

sol = Solution()

head = stringToListNode([0, 1, 2, 3, 4, 5, 6])
head = stringToListNode([])
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.reorderList(head))
