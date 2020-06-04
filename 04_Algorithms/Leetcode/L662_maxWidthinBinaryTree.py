# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        stack = [root,1]
        mark = []  # already visited place
        elementInEachLevel = [0]
        while stack:
            idx,depth = stack.pop()
            # print(idx)
            if len(elementInEachLevel) < depth:
                elementInEachLevel.append(1)
            else:
                elementInEachLevel[depth] += 1
            mark.append(idx)
            for child in [idx.left,idx.right]:  # ALL NEIGHBOR
                if not child in mark:
                    stack.append([child,depth+1])
        print(max(elementInEachLevel))
        return max(elementInEachLevel)

