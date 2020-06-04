# 使用列表来构建栈，其中在添加元素时同时添加元素和当前最小值
# （因为只允许从一端移动，所以最小值不会随顶端元素变动而变动）
# 栈的顺序就是列表中元素的顺序，添加和删除元素就是列表的append和pop
# 访问列表就可以得到第一个栈首元素值和最小值




class MinStack:

    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin));

    # @return nothing
    def pop(self):
        self.q.pop()


    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]


    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

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