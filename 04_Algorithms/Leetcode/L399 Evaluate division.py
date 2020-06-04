class UnionFindSet(object):
    """并查集"""
    def __init__(self, data_list):
        """初始化两个字典，一个保存节点的父节点，另外一个保存父节点的大小
        初始化的时候，将节点的父节点设为自身，size设为1"""
        self.father_dict = {}

        for node in data_list:
            self.father_dict[node] = [node,1]
            

    def find_head(self, node):
        father = self.father_dict[node][0]
        val = self.father_dict[node][1]

        if(node != father):  # node == father 代表这个节点是代表性节点，是真正得祖先
            self.father_dict[node][1] *= self.father_dict[father][1]
            father,fatherVal = self.find_head(father)
        self.father_dict[node][0] = father

        return father,self.father_dict[node][1]


    def countUp(self):
        for key in self.father_dict:
            self.find_head(key)

        return self.father_dict


    def union(self, node_a, node_b,valAB):
        """将两个集合合并在一起"""
        if node_a is None or node_b is None:
            return

        a_head,valA_head = self.find_head(node_a)
        b_head,valB_head = self.find_head(node_b)

        if(a_head != b_head):
            val = valA_head/(valB_head*valAB)
            self.father_dict[b_head] = [a_head,val]
            # print('self.father_dict',self.father_dict)

            
class Solution:
    def calcEquation(self, equations, values, queries):
        res = [-1 for _ in range(len(queries))]

        if equations == [[]] or equations == []:
            return res

        variableList = []
        for equation in equations:
            if not equation[0] in variableList:
                variableList.append(equation[0])
            if not equation[1] in variableList:
                variableList.append(equation[1])
        # print(variableList)
 

        element_UF = UnionFindSet(variableList)
        for i,equation in enumerate(equations):
            val = values[i]
            element_UF.union(equation[0],equation[1],val)
 

        father_dict = element_UF.countUp()
        print(father_dict)
        for j,query in enumerate(queries):
            # print(query)
            if query[0] in variableList and query[1] in variableList:
                # print('1')
                if query[0] == query[1]:
                    res[j] = 1
                    # print('3')

                elif father_dict[query[0]][0] == father_dict[query[1]][0]:
                    # print('4')
                    res[j] = father_dict[query[0]][1]/father_dict[query[1]][1]
                else:
                    # print('5')
                    res[j] = -1 
            else:
                # print('2')
                res[j] = -1
            # print(res)

        return res





# equations = [["a", "b"], ["b", "c"],['c','d']]
# values = [2.0, 3.0]
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]

sol = Solution()
# res = sol.calcEquation(equations,values,queries)
# print(res)
res = sol.calcEquation([["a","b"],["c","b"],["f","g"]],[2.0,3.0,4],
[["a","c"],["b","a"],["a","e"],["a","f"],["f","g"]])
print(res)

res = sol.calcEquation(
[["a","b"],["e","f"],["b","e"]],
[3.7,1.5,2.4],
[["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]])
print(res)