# -*- coding:utf-8 -*-
# 动态规划，为n的是为n-1和为n-2的组合，这个memoi也可以不需要，因为是前两项的之和
class Solution:
    def __init__(self):
        self.memoi = {1: 1, 2: 2}

    def rectCover(self, number):
        if number < 1:
            return 0
        elif number in self.memoi:
            return self.memoi[number]
        else:
            res = self.rectCover(number - 1) + self.rectCover(number - 2)
            self.memoi[number] = res
        return res


sol = Solution()
print(sol.rectCover(300))
