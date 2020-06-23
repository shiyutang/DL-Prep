# -*- coding:utf-8 -*-
from collections import Counter


class Solution:
    def Permutation(self, ss):
        prev = list(set(list(ss)))
        prev.sort()
        cnt = Counter(list(ss))
        def helper(prev, avai):
            for ele in prev:
                pass


        res = helper(prev, set(ss))
        return helper(ss)