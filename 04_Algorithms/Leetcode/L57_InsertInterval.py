## obsolete version: see another file please

class Solution:
    def insert(self, intervals, newInterval):
        if intervals == []:
            return [newInterval]
        else:
            starts,ends = [],[]
            for i in range(len(intervals)):
                starts.append(intervals[i][0])
                ends.append(intervals[i][1])
            startidx,endidx = 0,0
            for i in range(len(starts)):
                if starts[i]<=newInterval[0]:  # think the boundary
                    startidx = i+1          #insert interval start at
                if starts[i]<=newInterval[1]:
                    endidx = i+1
            delends = endidx -1
            if startidx == 0:
                insertStart = newInterval[0]
                delstart = startidx
            else:
                if newInterval[0] <= ends[startidx-1]:
                    insertStart = starts[startidx-1]
                    delstart = startidx-1
                else:
                    insertStart = newInterval[0]
                    delstart = startidx
            if endidx > len(intervals):
                insertend = newInterval[1]
            else:
                if ends[endidx-1]<=newInterval[1]:
                    insertend = newInterval[1]
                else:
                    insertend = ends[endidx-1]
            for i in range(max(delstart,0),delends+1):
                intervals.remove(intervals[delstart])
            intervals.insert(delstart,[insertStart,insertend])
            print((intervals))
            return intervals


sol = Solution()
# sol.insert([[1,3],[6,9]],[2,5])
# sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8])
# sol.insert([],[5,7])
# sol.insert([[1,5]],[1,7])
# sol.insert([[1,5]],[0,3])
sol.insert([[0,1],[5,5],[6,7],[9,11]],[12,21])
sol.insert([[1,5]],[0,0])
