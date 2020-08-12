# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# fast sort：退化到n2 时超时
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or head.next is None:
            return head

        pivot = head
        pointer = head.next
        Dummyleft, Dummyright = ListNode(0), ListNode(0)
        left, right = Dummyleft, Dummyright
        while pointer:
            if pointer.val <= pivot.val:
                left.next = pointer
                left = left.next
            else:
                right.next = pointer
                right = right.next
            pointer = pointer.next
        left.next, right.next = None, None  # 去除之前继承的影响

        lefthead = self.sortList(Dummyleft.next)
        righthead = self.sortList(Dummyright.next)

        if lefthead:
            head = lefthead
            while lefthead.next:
                lefthead = lefthead.next
            lefthead.next = pivot
        else:
            head = pivot
        pivot.next = righthead

        return head


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # termination.

        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None  # save and cut.
        # cut recursive.
        left, right = self.sortList(head), self.sortList(mid)

        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

head = stringToListNode([4, 5, 4, 3, 1, 0, 2])
head = stringToListNode([])
prettyPrintLinkedList(head)
sol = Solution()
prettyPrintLinkedList(sol.sortList(head))
