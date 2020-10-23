import bisect


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None
        self.levelDict = []
        self.data = []

    def insert(self, x):
        if not self.root:
            self.root = TreeNode(x)
            self.data = [x]
            self.levelDict = [1]
            return 1
        else:
            # insertNode = TreeNode(x)
            idx = bisect.bisect_left(self.data, x)
            # print(self.data, self.levelDict, x, idx)
            if idx == len(self.data):
                level = self.levelDict[idx-1] + 1
            elif idx == 0:
                level = self.levelDict[idx] + 1
            else:
                level = max(self.levelDict[idx], self.levelDict[idx - 1]) + 1
            self.data.insert(idx, x)
            self.levelDict.insert(idx, level)

            return self.levelDict[idx]


N = int(input().strip())
data = list(map(int, input().split(' ')))
sol = Solution()
for i in range(N):
    print(sol.insert(data[i]), end=' ')
    # sol.insert(data[i])