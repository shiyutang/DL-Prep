# -*- coding:utf-8 -*-
# 输入一个数组，可能为空，其中不包含重复数字
# 使用归并排序，拆分到最后合并，合并的结果再次用于合并
class Solution:
    def InversePairs(self, data):
        def helper(numlist):
            if len(numlist) == 1:
                return numlist, 0
            else:
                mid = len(numlist) // 2

                left, leftres = helper(numlist[:mid])
                right, rightres = helper(numlist[mid:])
                tmpres = leftres + rightres
                # print(leftres, rightres, numlist, mid)

                p1, p2 = len(left) - 1, len(right) - 1
                ret = []
                while len(ret) < len(left) + len(right):
                    if p1 < 0:
                        ret = right[:p2 + 1] + ret
                    elif p2 < 0:
                        ret = left[:p1 + 1] + ret
                    elif left[p1] > right[p2]:
                        tmpres += p2 + 1
                        ret.insert(0, left[p1])
                        p1 -= 1
                    else:
                        ret.insert(0, right[p2])
                        p2 -= 1
                return ret, tmpres

        if not data or len(data) == 1:
            return 0
        else:
            return helper(data)[1] % 1000000007


sol = Solution()
print(sol.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
