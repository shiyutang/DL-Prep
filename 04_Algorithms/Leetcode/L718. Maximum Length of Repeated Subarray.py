class Solution:
    def findLength(self, A, B):
        Alen,Blen = len(A),len(B)
        if not Alen or not Blen:
        	return 0
        buff = [[0 for i in range(Blen+1)] for _ in range(Alen+1)]
        for aidx in range(1,Alen+1):
        	for bidx in range(1,Blen+1):
        		if A[aidx-1] == B[bidx-1]:
        			print(aidx,bidx)
        			buff[aidx][bidx] = buff[aidx-1][bidx-1]+1
        return max(max(row) for row in buff)

sol = Solution()
# print(sol.findLength([1,2,3,2,1,4,2,5,2,7,2,7,2,8,2,8],[3,2,1,4,7,4,2,3,1,2,5,7,4,8,4,5]))
print(sol.findLength([1,2,3,2,1,4,3,6],[3,2,1,4,7]))