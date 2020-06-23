# -*- coding:utf-8 -*-
# 想利用三次二分是不靠谱的，因为大于上面一行某一列的不一定就大于这一列所有的值
# 方法： 设置一个关键节点，这个节点处在大于和小于的中间，类似于mid节点，那么根据大于还是小于就知道怎么判断
# 这个节点可以是右上角也可以是左下角
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if array == [[]] or array == []:
            return False
        i, j = 0, len(array[0]) - 1
        val = array[i][j]

        def isvalid(row, col):
            return 0 <= row < len(array) and 0 <= col < len(array[0])

        while 1:
            if target > val:
                i += 1
            elif target == val:
                return True
            else:
                j -= 1
            if not isvalid(i, j):
                return False
            val = array[i][j]
            # print(i, j)


sol = Solution()
print(sol.Find(10, [[1, 2, 3, 4],
                    [2, 6, 7, 9],
                    [5, 10, 11, 12], ]))
print(sol.Find(10, [[1, 2, 3, 4],
                    [2, 9, 11, 13],
                    [5, 10, 11, 12], ]))
print(sol.Find(10, [[]]))
