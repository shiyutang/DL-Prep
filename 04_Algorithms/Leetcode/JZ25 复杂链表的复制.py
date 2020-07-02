# -*- coding:utf-8 -*-
import json


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


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
    dummyRoot = RandomListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = RandomListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


# 给定头节点，打印链表
def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.label) + "->", end='')
        node = node.next

    if node:
        print(node.label)
    else:
        print("Empty LinkedList")


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        else:
            dummyroot = RandomListNode(0)
            pointer = dummyroot
            pointer2 = pHead
            memoi = {}

            # 复制整个链表先
            while pointer2:
                origincp = RandomListNode(pointer2.label)
                pointer.next = origincp
                memoi[pointer2] = origincp
                pointer = pointer.next
                pointer2 = pointer2.next

            # 重新开始指定随机指向节点
            pointer2 = pHead
            while pointer2:
                tmp = memoi[pointer2.random]
                memoi[pointer2].random = tmp
                pointer2 = pointer2.next
            return dummyroot.next


sol = Solution()
head = stringToListNode([1, 2, 3, 4, 5, 3, 5, None, 2, None])
prettyPrintLinkedList(head)
prettyPrintLinkedList(sol.Clone(head))
