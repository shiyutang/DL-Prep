import sys
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


# functions used to comunicate with the interactor (the other program)
# use this to the edge newly added edge.
# after using it you must provide your answer
# TL;DR get_edge() get_edge() is invalid
def get_edge():
    try:
        a = get_number()
        b = get_number()
    except:
        sys.exit(0)
    return a, b

# use this to set your answer
def set_answer(s):
    try:
        print(s)
        sys.stdout.flush()
        if s == 0:
            sys.exit(0)
    except:
        sys.exit(0)


class Graph: 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
        self.colorDict = {}
        self,vertices = []
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 


    def oddCycleCheck(self,city1,city2):
        self.answer = None
        color = 0
        def colorVertex(vertex,color):
            self.colorDict[vertex] = color
            for v in self.graph[vertex]:
                if not v in self.colorDict:
                    colorVertex(v,1-color)
                elif self.colorDict[v] == color:
                    print(v,'has color {} confilcted with {}'.format(color,vertex))
                    self.answer = 0
                    return          


        if not city1 in self.vertices and not city2 in self.vertices:
            self.colorDict[city1] = color
            self.colorDict[city2] = 1-color
            self.vertices.extend([city2,city1])
        elif city1 in self.vertices:
            self.colorDict[city2] = 1-self.colorDict[city1]
            self.vertices.append(city2)
        elif city2 in self.vertices:
            self.colorDict[city1] = 1-self.colorDict[city2]
            self.vertices.append(city1)
        else:
            if self.colorDict[city1] == self.colorDict[city2]:
                colorVertex(city2,1-self.colorDict[city1])

        if self.answer != None:
            return
        self.answer = 1


# use this to pass the first example
n = get_number()
answer = 1
cityGraph = Graph()
while answer == 1:
    city1,city2 = get_edge()
    cityGraph.addEdge(city2,city1)
    cityGraph.addEdge(city1,city2)
    print('cityGraph.graph',cityGraph.graph)
    cityGraph.oddCycleCheck(city1,city2)
    print('colorDict',cityGraph.colorDict)
    set_answer(cityGraph.answer)
