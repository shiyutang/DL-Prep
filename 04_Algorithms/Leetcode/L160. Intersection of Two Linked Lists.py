# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 走一遍，找到差，抛弃差，然后一一对比
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB

        while nodeA and nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next

        AStart = headA
        BStart = headB
        if nodeA:
            while nodeA:
                AStart = AStart.next
                nodeA = nodeA.next

        if nodeB:
            while nodeB:
                BStart = BStart.next
                nodeB = nodeB.next

        while AStart:
            if AStart == BStart:
                return AStart
            else:
                AStart = AStart.next
                BStart = BStart.next

        return None
