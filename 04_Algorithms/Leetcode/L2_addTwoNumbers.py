# 统一使用一个节点，在赋值时是让几个指针同时指向这个节点，
# 进一步修改某个指针下一位的指向可以同时修改几个指针的指向

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


class Solution:
    def addTwoNumbers(self, l1, l2):
        carryIn = False
        head = None
        while l1 or l2 or carryIn:
            number = 0
            if l1 and l2:
                number = l1.val + l2.val
            elif l1 or l2:
                number = l1.val if l1 else l2.val
            if carryIn:
                number += 1
                carryIn = False
            if number >= 10:
                carryIn = True
                number = number % 10
            node = ListNode(number)
            if not head:
                head = node
            else:
                tail.next = node
            tail = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head


def test():
    llist1 = Linkedlist()
    llist1.insertNode(2)
    llist1.insertNode(4)
    llist1.insertNode(3)
    llist2 = Linkedlist()
    llist2.insertNode(5)
    llist2.insertNode(6)
    llist2.insertNode(4)
    llist3 = Linkedlist()
    llist3.insertNode(9)
    llist3.insertNode(8)
    llist4 = Linkedlist()
    llist4.insertNode(1)

    sol = Solution()
    result = sol.addTwoNumbers(llist1.head, llist2.head)
    while result:
        print(result.val)
        result = result.next

    result = sol.addTwoNumbers(llist3.head, llist4.head)
    while result:
        print(result.val)
        result = result.next


test()
