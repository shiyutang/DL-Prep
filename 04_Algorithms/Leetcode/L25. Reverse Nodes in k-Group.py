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
    numbers = stringToIntegerList(input)
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
# main()

import sys 

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        flag = head
        k_cp = k
        queue = []
        while flag:
            queue.append(flag)
            k = k-1
            flag = flag.next
            print('queue'); print([item.val for item in queue])
            # print('k,flag.val', k,flag.val)
            if k == 0:
                if not queue[0] == head:
                    NextgroupPrev.next = queue[-1]

                now = flag
                for i in range(len(queue)):
                    prev = queue[i]
                    prev.next = now
                    now = prev

                if queue[0]== head:
                    head = now

                k = k_cp
                NextgroupPrev = queue[0]
                print('NextgroupPrev.val', NextgroupPrev.val)
                queue = []
            prettyPrintLinkedList(head)

        return head 


sol = Solution()

## generate linked list using input string and print it out prettily 
line  = input().strip('\n')
node = stringToListNode(line)
prettyPrintLinkedList(node)

k = int(input().strip('\n'))
headresult = sol.reverseKGroup(node,k)
print('the result is ')
prettyPrintLinkedList(headresult)


## O(1) space O(n) time using standard reversing
def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next