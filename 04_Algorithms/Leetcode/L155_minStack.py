class singleLinkedNode:
    def __init__(self, x):
        self.data = x
        self.next = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.datalist = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        node = singleLinkedNode(x)
        node.next = self.head
        self.head = node
        self.datalist.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.datalist.remove(self.head.data)
        self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.data

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.datalist)


def test():
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()

test()