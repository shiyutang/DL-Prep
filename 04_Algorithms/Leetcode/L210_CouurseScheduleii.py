class Solution:
    def findOrder(self, numCourses, prerequisites):
        # 拓扑排序检测有向图成环，无环输出坐标
        res = []
        stack = []
        incomeDegree = {} #每个节点入度
        point = {}    # 顶点指向确定
        if prerequisites==[]:
            return [i for i in range(numCourses-1,0,-1)]
        for i in range(len(prerequisites)):
            if incomeDegree.__contains__(prerequisites[i][0]):
                incomeDegree[prerequisites[i][0]] += 1
            else:
                incomeDegree[prerequisites[i][0]] = 1
            if point.__contains__(prerequisites[i][1]):
                point[prerequisites[i][1]].append(prerequisites[i][0])
            else:
                point[prerequisites[i][1]] = [prerequisites[i][0]]
        # print('point {}'.format(point))
        # print('incomeDegree {}'.format(incomeDegree))
        for key in point.keys():
            if not incomeDegree.__contains__(key):
                stack.append(key)
        # print(stack)
        while stack:
            a = stack.pop(-1)
            res.append(a)
            if point.__contains__(a):
                for idx in point[a]:
                    incomeDegree[idx] -= 1
                    if incomeDegree[idx] == 0:
                        stack.append(idx)
                        incomeDegree.pop(idx)
        if len(incomeDegree) >0:
            return []
        else:
            if len(res)<numCourses:
                for i in range(numCourses):
                    if not i in res:
                        res.insert(0,i)
            return res

sol = Solution()
res = sol.findOrder(3, [[1,0]])
print(res)
res = sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(res)

