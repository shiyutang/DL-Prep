# -*- coding:utf-8 -*-
# 指定一个插入奇数的指针，每次插入为O（1）, 插入了之后指针前移即可
class Solution:
    def reOrderArray(self, array):
        oddidx = 0
        for idx, num in enumerate(array):
            if num % 2 == 1:
                array.pop(idx)
                array.insert(oddidx, num)
                oddidx += 1
            # print(num,array)
        return array


sol = Solution()
print(sol.reOrderArray([1, 3, 5, 6, 7]))
print(sol.reOrderArray([]))
print(sol.reOrderArray([1]))
