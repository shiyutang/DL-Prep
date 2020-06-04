#Python program to print topological sorting of a DAG 
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        print(self.graph)
        visited = {}
        for key in self.graph:
            visited[key] = False
            for val in self.graph[key]:
                visited[val] = False
        print('visited',visited)
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for key in visited: 
            if visited[key] == False: 
                self.topologicalSortUtil(key,visited,stack) 
  
        # Print contents of stack 
        print(stack) 


# Python program to detect cycle  
# in a graph 
  
class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited,recStack = {},{}
        for key in self.graph:
            visited[key] = False
            recStack[key] = False
            for val in self.graph[key]:
                visited[val] = False
                recStack[val] = False

        for key in visited: 
            if visited[key] == False: 
                if self.isCyclicUtil(key,visited,recStack) == True: 
                    return True
        return False
  
g = Graph(4) 
g.addEdge('A', 'B'); 
g.addEdge('A', 'J'); 
g.addEdge('D', 'F'); 
g.addEdge('D', 'C');
g.addEdge('F', 'A'); 
g.addEdge('A', 'C'); 
g.addEdge('E', 'B'); 
g.addEdge('I', 'H'); 
g.addEdge('J', 'D'); 
g.addEdge('A', 'I'); 



if g.isCyclic() == 1: 
    print("Graph has a cycle")
else: 
    print("Graph has no cycle")
  
# Thanks to Divyanshu Mehta for contributing this code 

# g= Graph() 
# g.addEdge('C', 'A'); 
# g.addEdge('B', 'D'); 
# g.addEdge('C', 'B'); 
# g.addEdge('C', 'D'); 
# g.addEdge(2, 3); 
# g.addEdge(3, 1); 
  
# print("Following is a Topological Sort of the given graph")
# g.topologicalSort() 
# #This code is contributed by Neelam Yadav 