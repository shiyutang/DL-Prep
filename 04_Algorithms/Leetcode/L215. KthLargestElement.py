import random


class Solution:
    def quickSelect(self, a, l, r, index):
        q = self.randomPartition(a, l, r)
        if q == index:
            return a[q]
        else:
            return self.quickSelect(a, q + 1, r, index) if q < index else self.quickSelect(a, l, q - 1, index)

    def randomPartition(self, a, l, r):
        i = random.randint(l, r)
        a[i], a[r] = a[r], a[i]
        return self.partition(a, l, r)

    def partition(self, a, l, r):
        x = a[r]
        i = l - 1
        for j in range(l, r):
            if a[j] < x:
                i += 1
                a[i], a[j] = a[j], a[i]
        i += 1
        a[i], a[r] = a[r], a[i]
        return i

    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)