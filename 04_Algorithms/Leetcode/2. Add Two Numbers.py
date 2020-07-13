# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToIntegerList(input):
    # print('input',input)
    return json.loads(input)


# list 转换成链表
def stringToListNode(input):
    # Generate list from the input
    # numbers = stringToIntegerList(input)
    numbers = input
    # print('numbers', numbers)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


# 给定头节点，打印链表
def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")

# 重新创建一个链表记录结果，并且根据输入的不同形式得到结果，注意要向下传递来结束循环
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1, l2
        carry = 0
        dummy = ListNode(0)
        pt = dummy
        while node2 or node1 or carry:
            if node1 and node2:
                res = node1.val + node2.val + carry
                node2 = node2.next
                node1 = node1.next
            elif node1 and not node2:
                res = node1.val + carry
                node1 = node1.next
            elif not node1 and node2:
                res = node2.val + carry
                node2 = node2.next
            else:
                res = carry

            carry = res // 10
            residual = res % 10
            pt.next = ListNode(residual)
            pt = pt.next

        return dummy.next


head2 = stringToListNode([1, 8, 2, 9])
head1 = stringToListNode([9, 1, 8])
# head2 = stringToListNode([])
# head1 = stringToListNode([])
prettyPrintLinkedList(head1)
sol = Solution()
prettyPrintLinkedList(sol.addTwoNumbers(head1, head2))
