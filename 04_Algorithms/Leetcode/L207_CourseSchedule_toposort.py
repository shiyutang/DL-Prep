class Solution:
    def canFinish(self, numCourses, prerequisites):
        # 拓扑排序检测有向图成环，无环输出坐标
        res = []
        stack = []
        incomeDegree = {} #每个节点入度
        point = {}    # 顶点指向确定
        for i in range(len(prerequisites)):
            if incomeDegree.__contains__(prerequisites[i][0]):  #如果这个课程已经有先修课程了
                incomeDegree[prerequisites[i][0]] += 1    #先修课程数量加1
            else:
                incomeDegree[prerequisites[i][0]] = 1
            if point.__contains__(prerequisites[i][1]):   # 如果课程已经有后修课程
                point[prerequisites[i][1]].append(prerequisites[i][0])   #现在的后修课程加在之后
            else:
                point[prerequisites[i][1]] = [prerequisites[i][0]]
        print('point {}'.format(point))
        print('incomeDegree {}'.format(incomeDegree))
        for key in point.keys():          # 对于所有先修课程
            if not incomeDegree.__contains__(key):  # 入度为0的压入栈
                stack.append(key)
        print(stack)
        while stack:
            a = stack.pop(-1)
            res.append(a)
            if point.__contains__(a):     # 如果栈中元素（待删除顶点）有后修课程
                for idx in point[a]:      # 对于所有后修课程
                    incomeDegree[idx] -= 1   #入度-1
                    if incomeDegree[idx] == 0:   # 入度减少到0的顶点删除
                        stack.append(idx)
                        incomeDegree.pop(idx)
        if len(incomeDegree) >0:   #图中有顶点，成环，不能修完所有课程
            return False
        else:
            print(res)        #成换
            return True

sol = Solution()
res = sol.canFinish(2, [[1,0]])
print(res)