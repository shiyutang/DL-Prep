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


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToListNode(line)
            prettyPrintLinkedList(node)
        except StopIteration:
            break



class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        count = 0
        tmphead = head
        while tmphead:
        	count += 1
        	tmphead = tmphead.next
        if count == 1 or count == 0:
        	return head

        k = k%count

        if count == k or k == 0:
        	return head
        
        # here listLen >=2	
        splitPointpre = head
        splitPoint = head.next
        for i in range(count-k-1):
        	splitPoint = splitPoint.next
        	splitPointpre = splitPointpre.next

        # print(splitPoint.val)
        splitPointpre.next = None
        newhead = splitPoint
        while splitPoint.next:
        	splitPoint = splitPoint.next
        splitPoint.next = head

        return newhead

sol = Solution()
# head = stringToListNode([1,2,3,4,5])
# prettyPrintLinkedList(sol.rotateRight(head,2))
head = stringToListNode([0,1,2])
prettyPrintLinkedList(sol.rotateRight(head,4))



