class SortedStack:

    def __init__(self):
        self.data = []
        self.help = []

    def push(self, val: int) -> None:
        if self.data and self.data[-1] < val:
            while self.data and self.data[-1] < val:
                self.help.append(self.data.pop(-1))
        self.data.append(val)
        while self.help:
            self.data.append(self.help.pop(-1))
        # print(self.data)

    def pop(self) -> None:
        if not self.isEmpty():
            self.data.pop(-1)

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return not self.data


obj = SortedStack()
obj.push(1)
obj.push(3)
obj.push(2)
obj.push(0)
obj.pop()
print(obj.peek())
obj.pop()
print(obj.peek())
obj.pop()
print(obj.peek())
obj.pop()
print(obj.peek())
obj.pop()
print(obj.peek())
print(obj.isEmpty())
