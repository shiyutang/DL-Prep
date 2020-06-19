import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def stringToListNode(input):
    # Generate list from the input
    numbers = input

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


class Solution:
    def deleteDuplicates(self, head):
        point, newHead, newHead.next = head, ListNode(3), head
        prev = newHead
        duplicate = []
        while point:
            # print('point.val',point.val)
            if not point.next:
                if not point.val in duplicate:
                    prev.next = point
                    prev = prev.next
                break
            if point.val != point.next.val:
                if not point.val in duplicate:
                    duplicate = [point.val]
                    # print(prev.val)
                    prev.next = point
                    prev = prev.next
                    # print(prev.val)
                    # prettyPrintLinkedList(newHead)

                point = point.next
            else:
                duplicate = [point.val]
                point = point.next.next
        prev.next = None

        return newHead.next


def test(numbers):
    head = stringToListNode(numbers)
    # prettyPrintLinkedList(head)
    sol = Solution()
    prettyPrintLinkedList(sol.deleteDuplicates(head))


numbers = [1, 2, 3, 3, 4, 4, 5, 55]
test(numbers)
numbers = [1, 1, 1, 2, 3, 3, 4, 4, 5, 55]
test(numbers)
numbers = [0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
test(numbers)
numbers = [1, 2, 3, 3, 4, 4, 5]
test(numbers)
numbers = [1, 1, 1]
test(numbers)
