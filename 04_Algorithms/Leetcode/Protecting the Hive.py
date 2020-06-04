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

# normal UF
class UnionFindSet2(object):
    """并查集"""
    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def add_node(self,node):
        self.father_dict[node] = node
        self.size_dict[node] = 1


    def find_head(self, node):
        father = self.father_dict[node]
        if(node != father):  # node == father 代表这个节点是代表性节点，是真正得祖先
            father = self.find_head(father)
        self.father_dict[node] = father
        return father


    def countUp(self):
        for key in self.father_dict:
            self.find_head(key)
        resDict = {}
        for key in self.father_dict:
            if self.father_dict[key] in resDict:
                resDict[self.father_dict[key]].append(key)
            else:
                resDict[self.father_dict[key]] = [key]
        # print(resDict,self.father_dict)
        return resDict,self.father_dict


    def is_same_set(self, node_a, node_b):
        """查看两个节点是不是在一个集合里面"""
        return self.find_head(node_a) == self.find_head(node_b)


    def union(self, node_a, node_b):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head = self.find_head(node_a)
        b_head = self.find_head(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size
        # print('father after union',self.father_dict)



rows,cols = get_number(),get_number()
activeCells = []
for i in range(1,rows+1):
    row  = input().split(' ')
    for col,colItem in enumerate(row):
        if colItem is '1':
            activeCells.append((i,col+1))
# print('activeCells',activeCells)

numQ = get_number()
actions = []
for q in range(numQ):
    action = input().split(' ')
    actions.append(action)

# print('actions',actions)

union_find_set = UnionFindSet2(activeCells)
activeCellNeighborCnt = {}
visited = []
for cell in activeCells:
    visited.append(cell)
    neighborcnt = 0
    x,y = cell[0],cell[1]
    if x % 2 == 0:
        possible = [(x-1,y+1),(x-1,y),(x,y-1),(x,y+1),(x+1,y+1),(x+1,y)]
    else:
        possible = [(x-1,y-1),(x-1,y),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y)]
    
    for neigh in possible:
        if neigh in activeCells:
            if not neigh in visited:
                union_find_set.union(neigh,cell)
            neighborcnt += 1
    activeCellNeighborCnt[cell] = neighborcnt


hiveSet,fatherDict = union_find_set.countUp()
# print('activeCellNeighborCnt', activeCellNeighborCnt)
# print('hiveSet,fatherDict total', hiveSet,fatherDict)
for action in actions:
    action[1],action[2] = int(action[1]),int(action[2])
    if action[0] == 'a':
        neighborcnt = 0
        activeCells.append((action[1],action[2]))
        union_find_set.add_node((action[1],action[2]))
        
        x,y = action[1],action[2]
        if x % 2 == 0:
            possible = [(x-1,y+1),(x-1,y),(x,y-1),(x,y+1),(x+1,y+1),(x+1,y)]
        else:
            possible = [(x-1,y-1),(x-1,y),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y)]
        for neigh in possible:
            if neigh in activeCells:
                union_find_set.union(neigh,(action[1],action[2]))
                activeCellNeighborCnt[neigh] += 1
                neighborcnt+=1
                # print('union {} and {}'.format(neigh,(action[1],action[2])))
        activeCellNeighborCnt[(action[1],action[2])] = neighborcnt

        hiveSet,fatherDict = union_find_set.countUp()
        # print('hiveSet,fatherDict,activeCellNeighborCnt add {}'.format((action[1],action[2])), \
                               # hiveSet,fatherDict,activeCellNeighborCnt)



    elif action[0] == 'k':
        # print('(action[1],action[2]),fatherDict',(action[1],action[2]),fatherDict)
        if not (action[1],action[2]) in fatherDict:
            print(0)
        else:
            father = fatherDict[(action[1],action[2])]
            connectedComp,perimeter = hiveSet[father],0
            # print('(action[1],action[2]),connectedComp,activeCellNeighborCnt',
                # (action[1],action[2]),connectedComp,activeCellNeighborCnt)
            for cell in connectedComp:
                perimeter += 6- activeCellNeighborCnt[cell]

            print(perimeter)
