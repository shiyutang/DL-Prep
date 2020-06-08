from Debug_BST import TreeNode, PrintTree, list2Tree


# BFS with tag, 每次得到结果之后反向~
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        self.res = []

        def BFSwithTag(Q):
            while Q:
                (node, level) = Q.pop(0)
                if level > len(self.res) - 1:
                    self.res.append([node.val])
                    if level % 2 == 0 and level > 0:
                        self.res[-2].reverse()
                else:
                    self.res[level].append(node.val)
                if node.left is not None:
                    Q.append((node.left, level + 1))
                if node.right is not None:
                    Q.append((node.right, level + 1))
            if level % 2 == 1:
                self.res[-1].reverse()

        if root is not None:
            queue = [(root, 0)]
            BFSwithTag(queue)

        return self.res


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    nums = [1, 2, 1, 2, 1, 1, 2, 2, 1]
    nums = [1,2,3]
    head = list2Tree(nums)
    printT = PrintTree()
    printT.printTree(head)
    res = sol.zigzagLevelOrder(head)
    print(res)
    printT.printTree(head)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            data = []
            for __ in range(len1):
                num1 = random.sample([random.randint(1, 20) for i in range(20)] + [None], 1)
                data += num1
            print('data', data)
            head = list2Tree(data)
            printT.printTree(head)
            res = sol.zigzagLevelOrder(head)
            print(res)

test(Solution, True)




