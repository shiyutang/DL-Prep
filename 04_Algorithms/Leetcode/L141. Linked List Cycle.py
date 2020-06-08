import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToIntegerList(input):
    # print('input',input)
    return json.loads(input)


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


def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")


# 用两个快慢指针去寻找循环，因为每一步正好差一个，所以有圈一定可以碰上
# 另外，记得用快指针是否存在来判定会比慢指针快很多

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        else:
            point1 = head
            point2 = head

            while point2 and point2.next:
                point2 = point2.next.next
                if point1 is point2:
                    return True

                point1 = point1.next

            return False



