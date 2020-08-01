# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 通过快慢指针找到中间节点，然后将头尾翻转从中点之后和开始进行比较
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or head.next is None:
            return True
        p1 = p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        h = p1.next
        t = [p2, p2.next][p2.next is not None]

        def reverse(subhead, tail):
            if subhead == tail: # 相同则不需要翻转
                return subhead, tail
            current = subhead
            nextnode = current.next
            while nextnode.next:  # 反指并移动指针
                nextnxt = nextnode.next
                nextnode.next = current
                current = nextnode
                nextnode = nextnxt
            nextnode.next = current # 把最后一步指过来
            return tail, subhead

        h, t = reverse(h, t)
        p1.next = h
        t.next = None
        p2 = head
        prettyPrintLinkedList(head)
        p1 = p1.next
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True


sol = Solution()
from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

head = stringToListNode([1, 2, 3, 6, 2, 1])
head = stringToListNode([1])
prettyPrintLinkedList(head)
print(sol.isPalindrome(head))
