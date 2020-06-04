class Solution:
    def canFinish(self, numCourses, prerequisites):

        # we just need to contruct an DAG graph and check if there is cycle
        def helper(visited, recStack, prereq, cId):
            visited[cId] = True
            recStack[cId] = True
            if cId in prereq:      # 是先修课程
                for sId in prereq[cId]:   #
                    if visited[sId] == False:
                        if helper(visited, recStack, prereq, sId) == True:
                            return True
                    elif recStack[sId] == True:
                        return True

            recStack[cId] = False
            return False

        visited = [False] * numCourses   # 对第i个课程有没有访问
        recStack = [False] * numCourses
        prereq = {}  # 不同课程的先修课程

        for x, y in prerequisites:   # key为先修课程，val为课程
            if y not in prereq:
                prereq[y] = [x]
            else:
                prereq[y].append(x)

        for i in range(len(visited)):
            if not visited[i]:
                if helper(visited, recStack, prereq, i):
                    return False

        return True
