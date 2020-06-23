# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if not A:
            return A
        mat1 = [A[0]]
        mat2 = [A[-1]]
        for i in range(1, len(A)):
            mat1.append(A[i] * mat1[-1])
            mat2.insert(0, A[-1 - i] * mat2[0])
        ret = []
        for i in range(len(A)):
            if i - 1 < 0:
                ret.append(mat2[1])
            elif i + 1 == len(A):
                ret.append(mat1[-2])
            else:
                ret.append(mat1[i - 1] * mat2[i + 1])  # index 错误，除了本身索引越界，也可能是创造的list不够长
        return ret


sol = Solution()
print(sol.multiply([1, 2, 3, 4, 5, 6]))
print(sol.multiply([6]))
