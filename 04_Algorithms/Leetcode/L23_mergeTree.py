# Definition for singly-linked list.
# 初始判断时可以和后来的合并
# 注意考虑lists没有节点，有一个节点为空，只有一个空节点等极限情况
# 索引链表时，时刻考虑链表索引到后来节点为空的情况
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self,value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if (lists == []):
            return None
        headflag = False
        minIndex = 0
        head = lists[0]
        while not lists == [None] * len(lists):
            if lists[minIndex]:
                mintemp = lists[minIndex].val
            else:
                mintemp = 1000000000000000000000000000
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val < mintemp:
                    mintemp = lists[i].val
                    minIndex = i
            if not headflag:
                head,endpoint = lists[minIndex],lists[minIndex]
                headflag = True
            else:
                endpoint.next = lists[minIndex]
                endpoint = lists[minIndex]
            if lists[minIndex]:
                lists[minIndex] = lists[minIndex].next

        return head


def test():
    llist1 = Linkedlist()
    llist1.insertNode(1)
    llist1.insertNode(4)
    llist1.insertNode(5)
    llist2 = Linkedlist()
    llist2.insertNode(1)
    llist2.insertNode(3)
    llist2.insertNode(4)
    llist3 = Linkedlist()
    llist3.insertNode(2)
    llist3.insertNode(6)
    llist4 = Linkedlist()
    llist4.insertNode(1)
    lists = [llist1.head, llist2.head, llist3.head]
    lists = [llist4.head]

    sol = Solution()
    result = sol.mergeKLists(lists)
    while result:
        print(result.val)
        result = result.next

test()