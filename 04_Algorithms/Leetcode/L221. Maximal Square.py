class Solution:
    def maximalSquare(self, matrix):
        maxres = 0
        if not matrix or not matrix[0]:
            return maxres
        preacc = [0] * len(matrix[0])
        for i in range(len(matrix)):
            thisacc = [0] * len(matrix[0])
            for j in range(len(matrix[i])):
                if matrix[i][j] is '1':
                    thisacc[j] = preacc[j] + 1
            preacc = thisacc
            # print(thisacc)

            # cal the max base on this line
            stack = []
            record = [-1] * len(thisacc)
            for idx in range(0, len(thisacc)):
                if stack:
                    while stack and thisacc[idx] < thisacc[stack[-1]]:  # 更小是从左到右递增
                        if len(stack) == 1:
                            record[stack[-1]] = idx  # idx - -1
                        else:
                            record[stack[-1]] = idx - stack[-2] - 1  # (idx, stack[-2])
                        stack.pop()
                stack.append(idx)

            while stack:
                idx = stack.pop()
                if len(stack) == 0:
                    record[idx] = 1  # (-1, -1)
                else:
                    nextidx = stack[-1]
                    while thisacc[nextidx] >= thisacc[idx] and nextidx >= 0:  # 对于相等情况重新整理
                        nextidx -= 1

                    record[idx] = len(thisacc) - nextidx - 1  # (-1, nextidx)
            # print('record', record)

            for i in range(len(record)):
                maxres = max(maxres, min(thisacc[i], record[i]) ** 2)

        return maxres

class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        h = [0] * N
        maxw = 0
        for row in matrix:
            cw = 0
            for j, x in enumerate(row):
                h[j] = 0 if x is '0' else (h[j] + 1)  # 记录这一列的累加和
                if h[j] > maxw:
                    cw = cw + 1
                    if cw > maxw:           # maxw 代表这行能有的最大高度， cw 代表这个高度下的长度，当累计不到就消去
                        maxw, cw = cw, 0    # 分别计算大于
                else:
                    cw = 0
            print(maxw, cw)
        return maxw * maxw


sol = Solution()
data = [["1", "0", "0", "1", "1"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]
# data = [[]]
# data = [["1", "1", "0", "1"],
#         ["1", "1", "0", "1"],
#         ["1", "1", "1", "1"]]
res = sol.maximalSquare(matrix=data)
print(res)
