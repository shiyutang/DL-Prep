from collections import defaultdict


# 可以将h 数组替换为堆，减少max 的查询操作，增加了插入和删除时的logn时间，
class Solution:
    def getSkyline(self, buildings):
        start, end, endheight, startheight = [], [], defaultdict(list), defaultdict(list)
        ret = []

        for ele in buildings:
            start.append(ele[0])
            end.append(ele[1])
            endheight[ele[1]].append(ele[2])
            startheight[ele[0]].append(ele[2])
        end.sort()

        def helper(arr, ele):
            while arr and arr[0] == ele:
                arr.pop(0)
            return arr

        h, maxval = [], 0
        while start or end:
            if start and start[0] <= end[0]:
                p = start.pop(0)
                start = helper(start, p)
                h.extend(startheight[p])
                if p == end[0]:
                    for ele in endheight[end[0]]:
                        h.remove(ele)
                    p = end.pop(0)
                    end = helper(end, p)
            elif (start and start[0] > end[0]) or not start:
                for ele in endheight[end[0]]:
                    h.remove(ele)
                p = end.pop(0)
                end = helper(end, p)

            if not h:
                ret.append([p, 0])
            elif max(h) != maxval:
                maxval = max(h)
                ret.append([p, maxval])

        return ret


sol = Solution()
print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(sol.getSkyline([[0, 1, 3]]))
print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
print(sol.getSkyline([[3, 7, 8], [3, 8, 7], [3, 9, 6], [3, 10, 5], [3, 11, 4], [3, 12, 3], [3, 13, 2], [3, 14, 1]]))
