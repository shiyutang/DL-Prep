# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaveSequence1 = self.findSequence(root1)
        leaveSequence2 = self.findSequence(root2)
        return leaveSequence1==leaveSequence2

    def findSequence(self, root):
        node = root
        while node.left