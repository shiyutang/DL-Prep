from collections import defaultdict 

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

class Graph: 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    def DFS(self,start):
        neighbors = self.graph
        stack = [start]
        visited,res = {},[]
        fullvisit, partvisited,notvisit = 2,1,0
        visited[start] = partvisited
        while stack:
            vertexNow = stack[-1]
            try:
                neigh = neighbors[vertexNow].pop(0)
            except:
                vertexNow = stack.pop(-1)
                visited[vertexNow] = fullvisit
                res.append(vertexNow)
            else:
                if not neigh in visited:
                    visited[neigh] = partvisited
                    stack.append(neigh)

        return res[::-1]


n,m = get_number(),get_number()
graphCity = Graph()
# cityId are mapped to IDX: idx = cityid - 1
for i in range(m):
	city1,city2 = get_number(),get_number()
	graphCity.addEdge(city1-1,city2-1)
	graphCity.addEdge(city2-1,city1-1)

print('graphCity.graph',graphCity.graph)
visited = graphCity.DFS(0)
print(visited)