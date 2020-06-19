# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.str = []
        self.times = []

    # 返回对应char
    def FirstAppearingOnce(self):
        try:
            idx = self.times.index(1)
            return self.str[idx]

        except ValueError:
            return '#'

    def Insert(self, char):
        if char in self.str:
            self.times[self.str.index(char)] += 1
        else:
            self.str.append(char)
            self.times.append(1)
