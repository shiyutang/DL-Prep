# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head!=None) and (head.next!=None):
            oddList = [head]
            evenList = [head.next]
        while(1):
            try:
                if (evenList[-1].next!=None):
                    oddList[-1].next = evenList[-1].next
                    oddList.append(evenList[-1].next)
                else:
                    evenList[-1].next = None
                    break
                if oddList[-1].next!=None:
                    evenList[-1].next = oddList[-1].next
                    evenList.append((oddList[-1].next))
                else:
                    evenList[-1].next = None
                    break
            except UnboundLocalError:
                break
        try:
            oddList[-1].next = evenList[0]
        except UnboundLocalError:
            pass
        return head


def test():
    sol = Solution()
    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
    sol.oddEvenList(head)
    node = head
    while(node!=None):
        print(node.val)
        node = node.next

    sol = Solution()
    head = ListNode(2,ListNode(1,ListNode(3,ListNode(5,ListNode(4,ListNode(7,None))))))
    sol.oddEvenList(head)
    node = head
    while(node!=None):
        print(node.val)
        node = node.next

    head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,None))))
    sol.oddEvenList(head)
    node = head
    while(node!=None):
        print(node.val)
        node = node.next

    head = ListNode(1,None)
    sol.oddEvenList(head)
    node = head
    while(node!=None):
        print(node.val)
        node = node.next

    head = None
    sol.oddEvenList(head)
    node = head
    while(node!=None):
        print(node.val)
        node = node.next


test()
