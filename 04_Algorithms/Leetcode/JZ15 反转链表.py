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

 # 每次找到前面的一个，并接上，注意自己每次接的结点是什么，里面的next会不会是不需要的
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return pHead
        else:
            tmp = ListNode(pHead.val)  # 如果直接等于 pHead 的话，会导致也接上了pHead的next，这是不希望有的
            nextnode = pHead.next
            while nextnode:
                prev = nextnode.next
                nextnode.next = tmp
                tmp = nextnode
                nextnode = prev
            return tmp


sol = Solution()
head = stringToListNode([0, 1, 2])
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.ReverseList(head))
