import copy
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


# 方法：双指针法
# 假如例子如下：
# 图片说明
# 显然第一个公共结点为8，但是链表A头结点到8的长度为2，链表B头结点到8的长度为3，显然不好办？
# 如果我们能够制造一种理想情况，如下：
# 图片说明
# 这里先假设链表A头结点与结点8的长度 与 链表B头结点与结点8的长度相等，那么就可以用双指针。
#
# 初始化：指针ta指向链表A头结点，指针tb指向链表B头结点
# 如果ta == tb， 说明找到了第一个公共的头结点，直接返回即可。
# 否则，ta != tb，则++ta，++tb
# 所以现在的问题就变成，如何让本来长度不相等的变为相等的？
# 假设链表A长度为a， 链表B的长度为b，此时a != b
# 但是，a+b == b+a
# 因此，可以让a+b作为链表A的新长度，b+a作为链表B的新长度。
# 通过指针遍历的方式，遍历一个链表再遍历第二个，造成遍历两个相同长度的链表的假象，之后使用双指针一起移动

class Solution1:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1, p2 = pHead1, pHead2
        while p1 != p2:  # 必须是完全相同的结点（即下一个的指向相同）
            p1 = [p1.next, pHead2][p1.next is None]
            p2 = [p2.next, pHead1][p2.next is None]
        return p1


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        nodeset = set()
        p1, p2 = pHead1, pHead2
        while p1:
            nodeset.add(p1)
            p1 = p1.next

        while p2:
            if p2 in nodeset:
                return p2
            p2 = p2.next

        return None


head1 = stringToListNode([0, 1, 2])
head2 = copy.deepcopy(head1)
prettyPrintLinkedList(head1)
sol = Solution()
print(sol.FindFirstCommonNode(head1, head2))
