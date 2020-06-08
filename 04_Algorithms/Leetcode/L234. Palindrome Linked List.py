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


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        idx = len(tmp)//2 -1
        cmpIdx = [idx+1, idx+2][len(tmp)%2==1]
        while idx>=0:
            if tmp[idx] == tmp[cmpIdx]:
                cmpIdx += 1
                idx -= 1
            else:
                return False
        return True

# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    params = [[[1, 2, 3, 2, 1]],
              [[1,2]],
              [[0]],
              [[1,2,1]],
              [[1,2,2,1]],
              [[1,2,3,4,3,2]]
              ]
    for param in params:
        a = param[0]
        head = stringToListNode(a)
        prettyPrintLinkedList(head)
        res = sol.isPalindrome(head)
        print(' and the res is ', res)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)
            nums = list(set(nums))
            amount = random.randint(0, 100)
            print('the coinage are', nums)
            res = sol.coinChange(nums, amount)
            print(' and the minimum combinations for amount {} is {}'.format(amount, res))


test(Solution, False)