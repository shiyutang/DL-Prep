class Solution:
	def merge(self, intervals):
		if intervals == [] or intervals == [[]]:
			return intervals
		intervals = sorted(intervals,key = lambda val: val[0])
		preStart,preEnd = intervals[0][0],intervals[0][1]
		count = 1
		for i in range(1,len(intervals)):
			if intervals[i][0]<=preEnd:
				if intervals[i][1]>=preEnd:
					intervals[count-1] = [preStart,intervals[i][1]]
					preEnd = intervals[i][1]

			else:
				intervals[count] = intervals[i]
				preStart,preEnd = intervals[i][0],intervals[i][1]
				count+=1

		return intervals[0:count]

sol =Solution()
# print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
# print(sol.merge([[]]))
# print(sol.merge([[1,4],[2,3]]))
print(sol.merge([[1,2],[3,5],[6,7],[8,10],[12,16],[4,8]]))


