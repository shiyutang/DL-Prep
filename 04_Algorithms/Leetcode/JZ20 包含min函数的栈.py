# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.minval = []
        self.stack = []

    def push(self, node):
        self.stack.append(node)
        if not self.minval:
            self.minval = [node]
        else:
            self.minval.append(min(self.minval[-1], node))

    def pop(self):
        val = self.stack.pop(-1)
        self.minval.pop(-1)
        return val

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minval[-1]
