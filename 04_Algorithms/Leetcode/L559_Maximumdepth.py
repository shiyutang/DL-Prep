"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        stack = [[root,1]]
        mark = []  # already visited place
        alldepth = []
        while stack:
            idx,depth = stack.pop()
            print('tree_node',idx.val)
            alldepth.append(depth)
            mark.append(idx)
            for child in idx.children:  # ALL NEIGHBOR
                if not child in mark and child:
                    stack.append([child,depth+1])
                print('depth',depth)
            print('maxdepth',max(alldepth))
        return max(alldepth)