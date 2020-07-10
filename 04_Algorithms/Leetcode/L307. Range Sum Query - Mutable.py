# Segment Tree
# 看不懂的操作，还需要调试

class NumArray:
    def __init__(self, nums: list):
        n = len(nums)
        self.dataLen = n
        if n > 0:
            nbrNodes = 2 * n
            self.tree = [0 for _ in range(nbrNodes)]

            def helper():
                for i in range(n, 2 * n, 1):
                    self.tree[i] = nums[i - n]
                for i in range(n - 1, 0, -1):
                    self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

            helper()
            print(self.tree)

    def update(self, i: int, val: int) -> None:
        i += self.dataLen
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i = i // 2

    def sumRange(self, i: int, j: int) -> int:
        i += self.dataLen
        j += self.dataLen
        val = 0
        while i <= j:
            if i % 2 == 1:
                val += self.tree[i]
                i += 1
            if j % 2 == 0:
                val += self.tree[j]
                j -= 1
            i = i // 2
            j = j // 2
        return val


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5, 7, 9, 11]
obj = NumArray(nums)
param_2 = obj.sumRange(0, 7)
obj.update(3, 5)
param_3 = obj.sumRange(0, 7)
print(param_2, param_3)
