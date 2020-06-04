class Solution:
    def hIndex(self, citations):
        if citations != []:  # think about empty
            citations.sort(reverse=True)
            idx = 0
            while(idx<len(citations)):
                if citations[idx]<idx+1:
                    break
                else:
                    idx += 1
        else:
            return 0
        print(idx)
        return idx

sol = Solution()
sol.hIndex([9,4,9,5,6,9,4])