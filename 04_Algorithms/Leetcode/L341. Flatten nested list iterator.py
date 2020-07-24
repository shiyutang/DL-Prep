# 主要思想就是在是列表的时候展开加到所有缓存中，否则，返回
class NestedIterator:
    def __init__(self, nestedList: list):
        self.queue = nestedList

    def next(self) -> int:
        ret = self.queue.pop(0)
        return ret

    def hasNext(self) -> bool:
        while len(self.queue) >= 1:
            if isinstance(self.queue[0], int):
                return True
            else:
                self.queue = self.queue[0] + self.queue[1:]
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
sol = NestedIterator([[1, 1], 2, [1, 1]])
sol = NestedIterator([[1, [[[[[[[[[[[[]]]]]]]]]]]], 1], 2, [1, 1]])
while sol.hasNext():
    print(sol.next())
