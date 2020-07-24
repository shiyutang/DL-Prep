# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 除了-1层，其他不能没有，-1层只要没有了就不能再有
# BFS 层序遍历，加判断前面有没有出现过没有孩子的
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [root]
        nochild = False
        while queue:
            node = queue.pop(0)
            for nei in (node.left, node.right):
                if nochild:
                    if nei:
                        return False
                else:
                    if not nei:
                        nochild = True
                    else:
                        queue.append(nei)
        return True


from Debug_BST import list2Tree, PrintTree

sol = Solution()
data = [8, 6, 10, 5, 7, 9, 11]
data = [1, 2, 3, 4, 5, None, 7]
data = [1]
data = [1, 2, 3, 4, 2, 1, 4, None, None, 5]

tree = list2Tree(data)
printT = PrintTree()
printT.printTree(tree)

res = sol.isCompleteTree(tree)
print(res)
