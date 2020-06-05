# import sys
# sys.path.append('.')

from Debug_BST import TreeNode, PrintTree, list2Tree

## 二分搜索树的大小比较具有迭代性，只需要比较两个“相邻”结点的值就可以得出其是否满足要求
class Solution:
    def __init__(self):
        self.memoi = []

    def test(self, node, left, right):
        if node is None:
            tmp = None
        else:
            tmp = node.val
        print("examine whether node {} is between {} and {}".format(tmp, left, right))

    def isValidBST(self, root) -> bool:
        def childCmpKey(node, left, right):
            # self.test(node, left, right)
            if node is None:
                return True

            if node.val <= left or node.val >= right:
                return False
            else:
                return childCmpKey(node.left, left, node.val) and childCmpKey(node.right, node.val, right)

        return childCmpKey(root, -float('inf'), float('inf'))



#

# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    data = [5, 1, 7, None, None, 6, 8]
    # data = [2, 1, 3]
    # data = [3, 1, 5, 0, 2, 4, 6]
    data = [10, 5, 15, None, None, 6, 20]
    from L98_test_case import data

    tree = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree)

    res = sol.isValidBST(tree)
    print('the tree {} BST '.format(["isn\'t", "is"][res]))

    if random_samples:  # There are other rules constain the data, so it cannot be truly simulate by following code
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            data = []
            for __ in range(len1):
                num1 = random.sample([random.randint(1, 20) for i in range(20)] + [None], 1)
                data += num1
            print(data)
            tree = list2Tree(data)
            printT = PrintTree()
            printT.printTree(tree)

            res = sol.isValidBST(tree)
            print('the tree {} BST '.format(["isn\'t", "is"][res]))


test(Solution, True)
