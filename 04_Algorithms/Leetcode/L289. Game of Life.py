import copy
# 矩阵记得使用直接深拷贝，一定有用的

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def bordercheck(idx):
            idx1, idx2 = idx
            if 0 <= idx1 < len(board) and 0 <= idx2 < len(board[0]):
                return True
            return False

        tmp = copy.deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = [[i - 1, j - 1], [i - 1, j], [i - 1, j + 1], [i, j - 1],
                             [i, j + 1], [i + 1, j - 1], [i + 1, j + 1], [i + 1, j]]
                existneigh = map(bordercheck, neighbors)
                cnt = 0
                for index, ele in enumerate(existneigh):
                    if ele:
                        idx = neighbors[index]
                        if board[idx[0]][idx[1]] > 0:
                            cnt += 1

                if board[i][j] == 1:
                    if not 3 >= cnt >= 2:
                        tmp[i][j] = 0
                else:
                    if cnt == 3:
                        tmp[i][j] = 1
        board[:] = tmp
        print(board)


a = [[0, 1, 0],
     [0, 0, 1],
     [1, 1, 1],
     [0, 0, 1]]
#
# d = [[0, 0, 1],
#      [1, 0, 1],
#      [0, 0, 1],
#      [1, 0, 1]]
#
# c = [[0, 0, 0],
#      [1, 0, 1],
#      [0, 0, 1],
#      [0, 0, 1]]


# test
def test(method, random_samples=False):
    # test settings
    times = 10

    sol = method()
    sol.gameOfLife(a)

    if random_samples:
        import random

        for _ in range(times):
            len1 = random.randint(0, 20)
            nums = []
            for __ in range(len1):
                num1 = random.randint(1, 20)
                nums.append(num1)
            nums = list(set(nums))
            amount = random.randint(0, 100)
            print('the coinage are', nums)
            res = sol.coinChange(nums, amount)
            print(' and the minimum combinations for amount {} is {}'.format(amount, res))


test(Solution, False)
