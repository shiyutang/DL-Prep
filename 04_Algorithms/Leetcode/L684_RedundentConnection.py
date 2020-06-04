## 利用欧拉回路存在条件： 无向连通图中所有节点度为偶数
# 首先去掉所有度为奇数的节点和链接，如果存在剩余节点，剩余节点成环
# 输出边中包含两个剩余节点的最后一条边

class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 找到所有节点的度
        point = {}  #节点和节点之间的连接
        for i in range(edges):
            if point.__contains__(edges[i][0]):
                point[edges[i][0]].append(edges[i][1])
            else:
                point[edges[i][0]] = [edges[i][1]]
            if point.__contains__(edges[i][1]):
                point[edges[i][1]].append(edges[i][0])
            else:
                point[edges[i][1]] = [edges[i][0]]
        # 去除度为奇数的节点和其他联系
        for node in point.keys():
            if len(point[node]) == 1:
                stack = [point[node]]
                while stack:
                    pass
                for connectNode in point[node]:
                    point[connectNode].remove(node)
                    if len(point[connectNode]) == 1:
                        pass

                point.pop(i)