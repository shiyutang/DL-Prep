import random


# 自己实现 O(1) 的插入和删除，主要是删除需要知道删除哪个index，因此有个字典纪录，另外删除之后要维护一下防止其他index变化

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = []
        self.index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if not val in self.index:
            self.val.append(val)
            self.index[val] = len(self.val) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.val:
            i = self.index[val]
            self.val[i] = self.val[-1]
            self.index[self.val[-1]] = i
            self.val.pop(-1)
            del self.index[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """

        return int(random.sample(self.val, 1)[0])


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
val = 1
param_1 = obj.insert(val)
# param_2 = obj.remove(val)
param_3 = obj.getRandom()
print(param_3, param_1)
