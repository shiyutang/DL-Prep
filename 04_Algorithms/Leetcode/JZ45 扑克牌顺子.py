# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        cont = Counter(numbers)
        nbrzeros = cont[0]
        numbers.sort()
        print(numbers)
        diff = []
        for idx in range(nbrzeros+1, len(numbers)):
            diff.append(numbers[idx] - numbers[idx - 1] - 1)

        if -1 in diff:
            return False
        print(diff)
        return sum(diff) <= nbrzeros


sol = Solution()
# print(sol.IsContinuous([1, 3, 2, 6, 4]))
print(sol.IsContinuous([0, 3, 2, 6, 4]))
