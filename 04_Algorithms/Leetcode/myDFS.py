from collections import defaultdict 

## geeks for geeks version
class Graph: 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    # A function used by DFS 
    def DFSUtil(self, v, visited): 
        visited[v] = True
        print(v, end = ' ') 
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v): 
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 

        self.DFSUtil(v, visited) 


class Graph: 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def DFS(self,start):
    	stack = [start]
    	visited = []
    	while stack:
    		vertexNow = stack.pop(-1)
    		print(vertexNow)
    		visited.append(vertexNow)
    		for neigh in self.graph[vertexNow]:
    			if not neigh in visited and not neigh in stack:
    				stack.append(neigh)
    		# print('stack', stack)



mygraph = Graph()
# mygraph.addEdge(1,3)
# mygraph.addEdge(3,1)
# mygraph.addEdge(2,3)
# mygraph.addEdge(3,2)
# mygraph.addEdge(2,4)
# mygraph.addEdge(4,2)
# mygraph.addEdge(2,5)
# mygraph.addEdge(5,2)
# mygraph.addEdge(4,5)
# mygraph.addEdge(5,4)
mygraph.addEdge(0, 1) 
mygraph.addEdge(1, 0) 
mygraph.addEdge(0, 7)
mygraph.addEdge(7, 0) 
mygraph.addEdge(2,1) 
mygraph.addEdge(1, 2) 
mygraph.addEdge(1, 7) 
mygraph.addEdge(7,1) 
mygraph.addEdge(2, 3) 
mygraph.addEdge(3,2) 
mygraph.addEdge(2, 8) 
mygraph.addEdge(8, 2) 
mygraph.addEdge(2, 5) 
mygraph.addEdge(5, 2) 
mygraph.addEdge(3, 4) 
mygraph.addEdge(4, 3) 
mygraph.addEdge(3, 5) 
mygraph.addEdge(5, 3) 
mygraph.addEdge(4, 5) 
mygraph.addEdge(5, 4) 
mygraph.addEdge(5, 6) 
mygraph.addEdge(6, 5) 
mygraph.addEdge(6, 7) 
mygraph.addEdge(7, 6) 
mygraph.addEdge(6, 8) 
mygraph.addEdge(8, 6) 
mygraph.addEdge(7, 8) 
mygraph.addEdge(8, 7) 
print('Graph.graph',mygraph.graph)
mygraph.DFS(start = 1)


#非递归DFS
def depth_first_search2(self,root=None):
    stack = []
    order = []
    #self.visited[root] = True
    def dfs():
        while stack:
            node = stack[-1]
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    order.append(n)
                    stack.append(n)
                    self.visited[n] = True
                    break
            else:
                stack.pop()
    if root:
        stack.append(root)
        order.append(root)
        self.visited[root]=True
        dfs()

    for node in self.nodes():
        if node not in self.visited:
            stack.append(node)
            order.append(node)
            self.visited[node]=True
            dfs()

    self.visited = {}
    print order
    return order