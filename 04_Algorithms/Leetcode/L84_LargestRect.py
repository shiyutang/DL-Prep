class Solution:

    # @ rtype: int
    def largestRectangleArea(self, heights):

        if heights==[] or heights==[[]]*len(heights):
            return 0
        areamax = heights[0]
        for i in range(len(heights)):
            areasum = 0
            minheight = heights[i]
            for j in range(i, len(heights)):
                if heights[j]<minheight:
                    diff = (minheight-heights[j])*(j-i)
                    minheight = heights[j]
                    areasum = areasum + minheight-diff
                else:
                    areasum = areasum + minheight
                if areasum>areamax:
                    areamax = areasum
        return areamax

def test():
    sol = Solution()
    res = sol.largestRectangleArea([2,1,5,6,2,3])
    print(res)

    sol = Solution()
    res = sol.largestRectangleArea([3, 6, 5, 7, 4, 8, 1, 0])
    print(res)

test()
