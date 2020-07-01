# -*- coding:utf-8 -*-
from collections import Counter


# 排列就是每次选择一位放在前面，之后的继承
class Solution:
    def Permutation(self, ss):
        memoi = set()
        if not ss:
            return ''
        else:
            def helper(string, pt):
                if len(string) == pt + 1:
                    memoi.add(string)
                else:
                    for i in range(pt, len(string)):
                        tmp = string  # swap string
                        helper(tmp, pt + 1)

            helper(ss, pt=0)
