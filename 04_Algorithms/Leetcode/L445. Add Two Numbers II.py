# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        if not l1 and not l2:
            return l1
        p1, p2 = l1, l2
        while p1:
            stack1.append(p1)
            p1 = p1.next
        while p2:
            stack2.append(p2)
            p2 = p2.next

        carry = 0
        ret = []
        while stack2 or stack1:
            if stack1 and stack2:
                val1, val2 = stack1.pop(-1).val, stack2.pop(-1).val
            elif stack1:
                val1 = stack1.pop(-1).val
                val2 = 0
            else:
                val1 = 0
                val2 = stack2.pop(-1).val

            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            ret.append(ListNode(val))
        if carry:
            ret.append(ListNode(1))

        ret.reverse()
        for i, ele in enumerate(ret[:-1]):
            ele.next = ret[i + 1]

        return ret[0]


from L61_Rotate_List_linked_list_debug import stringToListNode, prettyPrintLinkedList

sol = Solution()
head1 = stringToListNode([])
prettyPrintLinkedList(head1)
head2 = stringToListNode([])
prettyPrintLinkedList(head2)
prettyPrintLinkedList(sol.addTwoNumbers(head1, head2))
