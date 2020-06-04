# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def canVisitAllRooms(self, root):
    queue = [root]
    mark = [root]  #already visited place
    while queue:
        node,width = queue.pop(0)
        # print(idx)
        for child in [root.left,root.right]:  # ALL NEIGHBOR
            if not child in mark:
                queue.append(child)