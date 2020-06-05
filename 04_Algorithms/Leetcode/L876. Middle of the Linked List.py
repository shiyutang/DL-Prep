# Definition for singly-linked list.
import copy
import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = copy.deepcopy(head)
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next

        middle = count // 2
        for i in range(middle):
            head = head.next
        return head


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    datalist = [1, 2, 3, 4, 5, 6]
    head = stringToListNode(datalist)
    prettyPrintLinkedList(head)

    res = sol.middleNode(head)
    print(' and the list after middle node is ', )
    prettyPrintLinkedList(res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)

            head = stringToListNode(nums)
            prettyPrintLinkedList(head)
            res = sol.middleNode(head)
            print(' and the list after middle node is ', prettyPrintLinkedList(res))


test(Solution, True)
