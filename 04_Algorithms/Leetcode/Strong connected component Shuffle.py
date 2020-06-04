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



from collections import defaultdict 
   
#This class represents an directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
          
        self.Time = 0
        self.res = []
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
          
   
    '''A recursive function that find finds and prints strongly connected 
    components using DFS traversal 
    u --> The vertex to be visited next 
    disc[] --> Stores discovery times of visited vertices 
    low[] -- >> earliest visited vertex (the vertex with minimum 
                discovery time) that can be reached from subtree 
                rooted with current vertex 
     st -- >> To store all the connected ancestors (could be part 
           of SCC) 
     stackMember[] --> bit/index array for faster check whether 
                  a node is in stack 
    '''
    def SCCUtil(self,u, low, disc, stackMember, st): 
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
        stackMember[u] = True
        st.append(u) 
  
        # Go through all vertices adjacent to this 
        for v in self.graph[u]: 
              
            # If v is not visited yet, then recur for it 
            if disc[v] == -1 : 
              
                self.SCCUtil(v, low, disc, stackMember, st) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                # Case 1 (per above discussion on Disc and Low value) 
                low[u] = min(low[u], low[v]) 
                          
            elif stackMember[v] == True:  
  
                '''Update low value of 'u' only if 'v' is still in stack 
                (i.e. it's a back edge, not cross edge). 
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v]) 
  
        # head node found, pop the stack and print an SCC 
        w = -1 #To store stack extracted vertices 
        if low[u] == disc[u]: 
            tmpres = []
            while w != u: 
                w = st.pop() 
                # print(w)
                tmpres.append(w) 
                stackMember[w] = False
                  
            # print('')
            self.res.append(tmpres)
              
      
  
    #The function to do DFS traversal.  
    # It uses recursive SCCUtil() 
    def SCC(self): 
   
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        disc = [-1] * (self.V) 
        low = [-1] * (self.V) 
        stackMember = [False] * (self.V) 
        st =[] 
          
  
        # Call the recursive helper function  
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if disc[i] == -1: 
                self.SCCUtil(i, low, disc, stackMember, st) 

        return self.res
  
  
   
families = get_number()
availableFamily = [None for j in range(families)]
g1 = Graph(families)
for i in range(families):
    visitF = list(map(int,input().strip().split()))
    available = []
    for j in range(families):
        if j != i and not j in visitF:
            g1.addEdge(i,j)

# print("SSC in first graph ")
res = g1.SCC() 
# print('res',res)
cnt = 0
for item in res:
    if len(item) == 1:
        cnt +=1
print(cnt)

