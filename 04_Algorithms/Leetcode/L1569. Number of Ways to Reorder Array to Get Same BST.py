import math


def comb(n, m):
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))


class Solution1:
    def helper(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return 1

        root = nums[0]
        left, right = [], []
        for num in nums[1:]:
            if num < root:
                left.append(num)
            else:
                right.append(num)

        leftcombs = self.helper(left)
        rightcombs = self.helper(right)
        print('left,leftcombs', left, leftcombs)
        print('right,rightcombs', right, rightcombs)
        res = ((((comb(len(nums) - 1, len(left)) % (self.mod)) * leftcombs) % (self.mod)) * rightcombs) % (self.mod)
        print('nums,res', nums, res)
        return int(res)

    def numOfWays(self, nums: list) -> int:
        self.mod = 10**9+7
        return int((self.helper(nums) - 1 + self.mod) % self.mod)


class TNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        self.size = 1
        self.ans = 0


class Solution:
    def numOfWays(self, nums: list) -> int:
        def insert(val: int):
            cur = root
            while True:
                cur.size += 1
                if val < cur.value:
                    if not cur.left:
                        cur.left = TNode(val)
                        return
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = TNode(val)
                        return
                    cur = cur.right

        def dfs(node: TNode):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            lsize = node.left.size if node.left else 0
            rsize = node.right.size if node.right else 0
            lans = node.left.ans if node.left else 1
            rans = node.right.ans if node.right else 1
            node.ans = c[lsize + rsize][lsize] * lans * rans % mod

        n = len(nums)
        if n == 1:
            return 0

        mod = 10 ** 9 + 7
        c = [[0] * n for _ in range(n)]
        c[0][0] = 1
        for i in range(1, n):
            c[i][0] = 1
            for j in range(1, n):
                c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % mod

        root = TNode(nums[0])
        for i in range(1, n):
            val = nums[i]
            insert(val)

        dfs(root)
        return (root.ans - 1 + mod) % mod


sol = Solution1()
print(sol.numOfWays(
    nums=[10, 23, 12, 18, 4, 29, 2, 8, 41, 31, 25, 21, 14, 35, 26, 5, 19, 43, 22, 37, 9, 20, 44, 28, 1, 39, 30, 38, 36,
          6, 13, 16, 27, 17, 34, 7, 15, 3, 11, 24, 42, 33, 40, 32]))  # 182440977
# print(sol.numOfWays(nums=[2, 1, 3]))
# print(sol.numOfWays(nums=[3, 4, 5, 1, 2]))
# print(sol.numOfWays(nums=[1, 2, 3]))
# print(sol.numOfWays(nums=[3, 1, 2, 5, 4, 6]))
# print(sol.numOfWays(nums=[9, 4, 2, 1, 3, 6, 5, 7, 8, 14, 11, 10, 12, 13, 16, 15, 17, 18]))
