# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
[3,9,20,15,7]
root = TreeNode(3)
a = TreeNode(9)
B = TreeNode(20)
C = TreeNode(15)
d = TreeNode(7)
root.left = a
root.right = B
B.left = C
B.right = d
import time
import copy
class Solution:
    def allSubNodeIsLeaf(self, subnode):
        for node in subnode:
            if not (node.left == None and node.right == None):
                return False
        return True

    def averageOfLevels(self, root):
        time1 = time.clock()
        if root == []:
            return []
        subnode = [root]
        allVal = []
        time2 = time.clock()
        while not self.allSubNodeIsLeaf(subnode):
            levelVal = []
            nextsubnode = []
            for node in subnode:
                levelVal.append(node.val)
                if node.left != None:
                    nextsubnode.append(node.left)
                if node.right != None:
                    nextsubnode.append(node.right)
            subnode = copy.deepcopy(nextsubnode)
            allVal.append(levelVal)
        time3 = time.clock()

        levelVal = []
        for node in subnode:
            levelVal.append(node.val)
        allVal.append(levelVal)
        res = []
        for levelval in allVal:
            res.append(sum(levelval) / len(levelval))
        time4 = time.clock()
        print(time2-time1)
        print(time3-time2)
        print(time4-time3)
        return res

sol = Solution()
time5 = time.clock()
res = sol.averageOfLevels(root)
time6 = time.clock()
print(time6-time5)
print(res)