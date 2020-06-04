class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0]==[]:
            return False
        idx = [0,0]
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
        diagnal = []
        print(matrix)
        while matrix[idx[0]][idx[1]]!=target:
            if idx[1]>=len(matrix[0])-1 or matrix[idx[0]][idx[1]+1] >target:
                if idx[0]+1>len(matrix):
                    return False
                elif matrix[idx[0]+1][idx[1]] > target:
                    print('start diagonal')
                    break
                elif matrix[idx[0]+1][idx[1]] == target:
                    return True
                else:
                    idx[0] += 1
                    print('push left')
                    print(matrix[idx[0]][idx[1]])
                    continue
            elif matrix[idx[0]][idx[1]+1] == target:
                return True
            else:
                idx[1] += 1
                print('push right')
                print(matrix[idx[0]][idx[1]])

        for i in range(idx[0] + idx[1] + 1):
            if i<=len(matrix)-1 and idx[0] + idx[1] - i<=len(matrix[0])-1 and idx[0] + idx[1] - i>=0 and i>=0:
                diagnal.append([i, idx[0] + idx[1] - i])
        print(diagnal)
        while diagnal:
            diagidx = diagnal.pop()
            if matrix[diagidx[0]][diagidx[1]] == target:
                return True
            elif diagidx[1]+1<len(matrix[0]):
                if matrix[diagidx[0]][diagidx[1]+1] ==target:
                    return True
            elif diagidx[0]+1<len(matrix):
                if matrix[diagidx[0]+1][diagidx[1]] ==target:
                    return True
        return False



sol = Solution()
# res = sol.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],
#                   [3,6,9,16,22],[10,13,14,17,24],
#                   [18,21,23,26,30]],33)
# print(res)
# res = sol.searchMatrix([[25,28,33]],33)
# print(res)
# res = sol.searchMatrix([[-1,3]],1)
# print(res)
res = sol.searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]],13)
print(res)
