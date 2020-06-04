class MinStack:

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append((x));

    # @return poped content
    def pop(self):
        content = self.q.pop()
        return content

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1]


    def isEmpty(self):
        if len(self.q) == 0:
            return True
        else:
            return False


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = MinStack()
        self.stack2 = MinStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        content = self.stack2.pop()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return content

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.pop())
        content = self.stack2.top()
        while not self.stack2.isEmpty():
            self.stack1.push(self.stack2.pop())
        return content

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        flag = self.stack1.isEmpty()
        return flag

def test():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    content = myQueue.peek()
    print(content)
    c = myQueue.pop()
    print(c)
    myQueue.empty()

test()