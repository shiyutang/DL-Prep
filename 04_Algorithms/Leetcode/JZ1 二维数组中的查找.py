# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        tmp = array[0]
        find = False

        def bisectfind(alist, target):
            low, high = 0, len(alist) - 1
            mid = (low + high) // 2
            while high > low:
                if alist[mid] > target:
                    high = mid - 1
                elif alist[mid] == target:
                    global find
                    find = True
                    return mid
                else:
                    low = mid
            return low

        res = bisectfind(tmp, target)
        if find:
            return find

        tmp = []
        for i in range(len(array)):
            tmp.append(array[i][res])

        res = bisectfind(tmp, target)
        if find:
            return find

        tmp = array[res]
        _ = bisectfind(tmp, target)
        return find


sol = Solution()
print(sol.Find(10, [[1, 2, 3, 4],
                    [2, 6, 7, 9],
                    [5, 9, 11, 12], ]))
