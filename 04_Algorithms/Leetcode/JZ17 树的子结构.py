# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        else:
            def issub(node1, node2):
                if not node2:
                    return True
                elif not node1:
                    return False
                else:
                    return node1.val == node2.val and issub(node1.left, node2.left) and issub(node1.right, node2.right)

            def pretravese(node):
                if node:
                    res = pretravese(node.left)
                    if res:
                        return True
                    res = pretravese(node.right)
                    if res:
                        return True
                    if node.val == pRoot2.val:
                        if issub(node, pRoot2):
                            return True

            result = pretravese(pRoot1)
            return [result, False][result is None]


from Debug_BST import list2Tree, PrintTree


def test(method):
    # test settings

    sol = method()
    data = [8, 8, 7, 9, 3, None, None, None, None, 4, 7]
    data2 = [8, 9, 2]

    tree = list2Tree(data)
    printT = PrintTree()
    printT.printTree(tree)
    tree2 = list2Tree(data2)
    printT = PrintTree()
    printT.printTree(tree2)

    res = sol.HasSubtree(tree, tree2)
    print(res)


test(Solution)
