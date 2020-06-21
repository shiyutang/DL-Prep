# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        sLen = len(s)
        idx = n % sLen
        return s[idx:] + s[:idx]
