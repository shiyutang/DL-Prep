class SortedStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        if not self.data:
            self.data.append(val)
        else:
            def helper(num):
                low, high = 0, len(self.data) - 1
                mid = low + (high - low) // 2
                while low < high:
                    if self.data[mid] < num:
                        low = mid + 1
                    elif self.data[mid] == num:
                        return mid
                    else:
                        if mid - 1 >= 0:
                            if self.data[mid - 1] < num:
                                return mid
                            elif self.data[mid - 1] == num:
                                return mid - 1
                            else:
                                high = mid
                        else:
                            return mid
                    mid = low + (high - low) // 2
                return mid

            if self.data[-1] < val:
                self.data.append(val)
            else:
                idx = helper(val)
                self.data.insert(idx, val)

    def pop(self) -> None:
        if not self.isEmpty():
            self.data.pop(0)

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[0]

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
