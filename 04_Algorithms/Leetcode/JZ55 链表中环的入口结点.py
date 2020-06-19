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

class Solution:
    def EntryNodeOfLoop(self, pHead):
        slowvisit = set()
        if pHead:
            slow = pHead
            while slow:
                if slow in slowvisit:
                    return slow
                slowvisit.add(slow)
                slow = slow.next
            return 
        else:
            return

head = stringToListNode([1,0])
sol = Solution()
res = sol.EntryNodeOfLoop(head)
print(res)