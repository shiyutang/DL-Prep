# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.str = []
        self.times = []

    # 返回对应char
    def FirstNotRepeatingChar(self, s):
        for char in s:
            if char in self.str:
                self.times[self.str.index(char)] += 1
            else:
                self.str.append(char)
                self.times.append(1)

        try:
            idx = self.times.index(1)
            return s.index(self.str[idx])

        except ValueError:
            return -1


sol = Solution()
print(sol.FirstNotRepeatingChar('google'))
