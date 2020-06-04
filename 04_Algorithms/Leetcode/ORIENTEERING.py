# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

import sys 
import math
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print("Vertex \tDistance from Source")
        for node in range(self.V): 
            print(node, "\t", dist[node] )
  

    def addEdge(self,row,col,distance):
        self.graph[pos] = distance

    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
        min = sys.maxsize 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  

    def dijkstra(self, src): 
  
        dist = [sys.maxsize] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shortest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]: 
                        dist[v] = dist[u] + self.graph[u][v] 
        self.dist = dist
        self.printSolution(dist) 

def calDistance(start,end,runnability,Hightlevel):
    ra,rb = runnability[start[0]][start[1]],runnability[end[0]][end[1]]
    ha,hb = Hightlevel[start[0]][start[1]],Hightlevel[end[0]][end[1]]
    # print('ra,rb,ha,hb',ra,rb,ha,hb)
    # print('distance',((ra+rb)/2),(math.exp(3.5*abs((hb-ha)/10+0.05))))
    return (ra+rb)/2*math.exp(3.5*abs((hb-ha)/10+0.05))

def fun(x):
    return x[0]>=0 and x[0]<x[2] and x[1]>=0 and x[1]<x[3]  

n,m,p = get_number(),get_number(),get_number()
points = []
for i in range(p+1):
    points.append([get_number(),get_number()])

runnability = [[0 for i in range(m)] for j in range(n)]
Hightlevel = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        runnability[i][j] = get_number()
for i in range(n):
    for j in range(m):
        Hightlevel[i][j] = get_number()
# print('runnability,Hightlevel',runnability,Hightlevel)

numVertex = n*m
g = Graph(numVertex) 
for i in range(n):
    for j in range(m):
        for point in filter(fun,[[i-1,j,n,m],[i+1,j,n,m],[i,j-1,n,m],[i,j+1,n,m]]):
            distance  = calDistance((i,j),point,runnability,Hightlevel)
            g.graph[i*m+j][point[0]*m+point[1]] = distance


res = 0
for i,point in enumerate(points):
    if i+1<len(points):
        pointIdx = point[0]*m+point[1]
        g.dijkstra(pointIdx)
        nextPointIdx = points[i+1][0]*m + points[i+1][1]
        # print('point,nextPointIdx',point,pointIdx, points[i+1], nextPointIdx)

        res = res + g.dist[nextPointIdx]
print('res', res)